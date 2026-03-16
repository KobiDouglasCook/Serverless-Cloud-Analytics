async function shorten() {
    const longUrl = document.getElementById("longUrl").value;

    const response = await fetch("/shorten", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ longUrl })
    });

    const data = await response.json();
    document.getElementById("result").innerText = data.shortUrl || data.error;
}
