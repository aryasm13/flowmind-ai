async function runWorkflow() {
    const input = document.getElementById("inputText").value;

    const res = await fetch("http://127.0.0.1:5000/run-workflow", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ input })
    });

    const data = await res.json();

    document.getElementById("output").innerText =
        JSON.stringify(data, null, 2);
}