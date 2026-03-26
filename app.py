from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime

from graph.workflow import app as workflow_app

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"status": "FlowMind API running"}

@app.route("/run-workflow", methods=["GET"])
def test_run():
    return {"message": "Use POST request with JSON body"}

@app.route("/run-workflow", methods=["POST"])
def run_pipeline():
    try:
        data = request.json
        input_text = data.get("input", "")

        if not input_text:
            return jsonify({"error": "No input provided"}), 400

        result = workflow_app.invoke({"input": input_text})

        log_entry = {
            "timestamp": str(datetime.now()),
            "input": input_text,
            "output": result
        }

        try:
            with open("data/logs.json", "r") as f:
                logs = json.load(f)
        except:
            logs = []

        logs.append(log_entry)

        with open("data/logs.json", "w") as f:
            json.dump(logs, f, indent=2)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/logs", methods=["GET"])
def get_logs():
    try:
        with open("data/logs.json", "r") as f:
            logs = json.load(f)
        return jsonify(logs)
    except:
        return jsonify([])


if __name__ == "__main__":
    app.run(debug=True)