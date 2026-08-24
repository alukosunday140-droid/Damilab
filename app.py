from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error loading home page: {e}", 500

@app.route('/about')
def about():
    try:
        return render_template('about.html')
    except Exception as e:
        return f"Error loading about page: {e}", 500

@app.errorhandler(404)
def page_not_found(e):
    return "Page not found - 404", 404

if __name__ == '__main__':
    app.run(debug=True)
