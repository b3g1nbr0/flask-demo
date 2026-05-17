from flask import Flask
from flask_wtf.csrf import CSRFProtect
from .routes import main

csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'change-this-very-secret-key'
    csrf.init_app(app)
    app.register_blueprint(main)
    return app
