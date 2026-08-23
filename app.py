from flask import Flask, render_template, jsonify

app = Flask(__name__)

courses = [
    {"id": 1, "title": "Intro to Python", "level": "Beginner", "duration": "4 weeks"},
    {"id": 2, "title": "Digital Marketing 101", "level": "Beginner", "duration": "3 weeks"},
    {"id": 3, "title": "Data Analysis with Excel", "level": "Intermediate", "duration": "5 weeks"}
]

@app.route("/")
def home():
    return render_template("index.html", course_count=len(courses))

@app.route("/api/courses")
def get_courses():
    return jsonify(courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
