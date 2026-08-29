from flask import Flask, flash, jsonify, redirect, render_template, url_for

from .config import DevelopmentConfig
from .courses import get_courses
from .forms import ContactForm


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)

    app.config.from_object(config_class)
    app.config["JSON_SORT_KEYS"] = False

    @app.route("/")
    def home():
        courses = get_courses()

        return render_template(
            "index.html",
            course_count=len(courses),
        )

    @app.route("/health")
    def health():
        return jsonify({
            "status": "ok"
        })

    @app.route("/api/courses")
    def courses():
        return jsonify({
            "courses": get_courses()
        })

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        form = ContactForm()

        if form.validate_on_submit():
            flash("Your message has been received.")
            return redirect(url_for("contact"))

        return render_template("Contact.html", form=form)

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
