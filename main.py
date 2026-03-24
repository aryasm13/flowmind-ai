from graph.workflow import build_workflow
import json

def run():
    app = build_workflow()

    with open("data/sample_inputs.json") as f:
        data = json.load(f)

    input_text = data[0]["input"]

    result = app.invoke({"input": input_text})

    print("\n================ FINAL RESULT ================\n")

    print("Tasks:")
    print(result.get("tasks"))

    print("\nSteps:")
    print(result.get("steps"))

    print("\nValidation Status:")
    print(result.get("status"))

    if result.get("status") == "FAIL":
        print("\nIssues:")
        print(result.get("issues"))

        print("\nFixes:")
        print(result.get("recovery"))

    print("\n=============================================\n")

if __name__ == "__main__":
    run()