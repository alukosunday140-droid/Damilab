from flask import Flask, jsonify

from .config import DevelopmentConfig


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)
    app.config["JSON_SORT_KEYS"] = False

    @app.route("/")
    def home():
        return jsonify({
            "message": "Damilab API is running",
            "version": "1.0.0"
        })

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok"
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "error": "Not found"
        }), 404

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({
            "error": "Internal server error"
        }), 500

    return app


app = create_app()
