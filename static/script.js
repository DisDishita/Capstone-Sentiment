async function analyze() {
    const text = document.getElementById("userText").value;
    const resultDiv = document.getElementById("result");

    if (!text) {
        resultDiv.innerText = "Please enter some text.";
        return;
    }

    resultDiv.innerText = "Analyzing...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text })
        });

        const data = await response.json();
        resultDiv.innerText = "Sentiment: " + data.prediction;
    } catch (error) {
        console.error(error);
        resultDiv.innerText = "Error connecting to API.";
    }
}