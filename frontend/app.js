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

    // Update UI with short URL + dynamic analytics button
    document.getElementById("result").innerHTML = `
        <p><strong>Short URL:</strong> 
            <a href="${payload.shortUrl}" target="_blank">${payload.shortUrl}</a>
        </p>

        <a 
            href="/analytics.html?code=${payload.shortCode}"
            style="
                display: inline-block;
                margin-top: 12px;
                padding: 10px 16px;
                background-color: #2563eb;
                color: white;
                border-radius: 6px;
                text-decoration: none;
                font-weight: 500;
            "
        >
            View Analytics for This URL
        </a>
    `;
}
