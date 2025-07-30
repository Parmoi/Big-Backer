from config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create SQLAlchemy instance
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    app.secret_key = "356fP]}'I{oMOU[x5_X^-mD!V?~o.B"

    from .routes import main
    app.register_blueprint(main)    # Register the blueprint

    db.init_app(app)

    # Creates tables that do not exist in the db
    with app.app_context():
        db.create_all()

    return app