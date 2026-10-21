import os
from flask import Flask, redirect, abort

app = Flask(__name__)

TARGET_URL = os.environ.get(
    "TARGET_URL",
    "https://example.com"
)

@app.route("/oudbIS")
def go():
    if not TARGET_URL.startswith("https://"):
        abort(500)

    return redirect(TARGET_URL, code=302)

@app.route("/")
def home():
    return "Redirect service is running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))