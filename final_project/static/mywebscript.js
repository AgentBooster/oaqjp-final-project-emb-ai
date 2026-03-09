window.RunEmotionDetection = async ()=>{
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    console.log("Button clicked! Parsing:", textToAnalyze);
    try {
        let response = await fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze));
        let text = await response.text();
        document.getElementById("system_response").innerHTML = text;
    } catch(err) {
        console.error(err);
    }
}
