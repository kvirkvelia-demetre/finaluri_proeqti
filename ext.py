from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "21"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db?timeout=30"
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "connect_args": {
        "check_same_thread": False,
        "timeout": 30
    }
}

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "login"
login_manager.login_message = None