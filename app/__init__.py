from flask import Flask
from .models import db
from .routes import main

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    app.register_blueprint(main)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
