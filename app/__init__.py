    from flask import Flask, jsonify

    app = Flask(__name__)

    @app.route("/")
    def home():
        return jsonify({
            "message": "Damilab API is running",
            "version": "1.0.0"
        })

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})
