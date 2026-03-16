async function shorten() {
    const longUrl = document.getElementById("longUrl").value;

    const response = await fetch("/shorten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ longUrl })
    });

    const data = await response.json();
    console.log("RAW /shorten RESPONSE:", data);

    const payload = data;

    document.getElementById("result").innerText =
        payload.shortUrl || payload.error || "Unexpected response";
}
