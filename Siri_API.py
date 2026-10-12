from flask import Flask, request
import subprocess

app = Flask(__name__)


# API key
SECRET = "78285"

def auth():
    return request.args.get("key") == SECRET


@app.route("/restart")
def restart():
    if not auth():
        return "Unauthorized", 403

    subprocess.run(["shutdown", "/r", "/t", "0"], check=True)
    return "Done. Restarting your PC."


@app.route("/shutdown")
def shutdown():
    if not auth():
        return "Unauthorized", 403

    subprocess.run(["shutdown", "/s", "/t", "0"], check=True)
    return "Done. Shutting down your PC."


app.run(host="0.0.0.0", port=5000)