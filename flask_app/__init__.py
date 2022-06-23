from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "Hello World!"

    return app

if __name__ == "__main__":
    app = creat_app()
    app.run(debug=True)