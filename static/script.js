async function analyze() {
    const text = document.getElementById("userText").value;
    const resultDiv = document.getElementById("result");

    if (!text) {
        resultDiv.innerText = "Please enter some text.";
        return;
    }

    resultDiv.innerText = "Analyzing...";

    try {
        const response = await fetch("/predict", {   // ✅ FIXED
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
