from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "356fP]}'I{oMOU[x5_X^-mD!V?~o.B"

    from .routes import main
    app.register_blueprint(main)    # Register the blueprint

    return app