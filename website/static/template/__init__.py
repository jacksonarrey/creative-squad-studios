from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRETE_KEY'] = 'jacky arrey'

    return app