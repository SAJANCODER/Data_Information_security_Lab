from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, HTTPS Flask Server!"

if __name__ == "__main__":
    # Use adhoc SSL - Flask automatically generates temporary certificates
    app.run(host="0.0.0.0", port=5000, ssl_context='adhoc')
