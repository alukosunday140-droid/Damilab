
    from flask import Flask

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev-key'

    @app.route('/')
    def home():
        return "Hello Damilab"

    if __name__ == '__main__':
        app.run(debug=True)
