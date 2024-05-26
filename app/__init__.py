from flask import Flask

def create_app():
    app = Flask(__name__)
    from .weather import weather_bp
    app.register_blueprint(weather_bp)
    return app
