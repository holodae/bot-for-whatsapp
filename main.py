from flask import Flask

from src.auth.controllers.auth import AuthController 

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)

        self.authBp = AuthController().authBp
        self.app.register_blueprint(self.authBp, url_prefix="/auth")

    def start(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    my_app = FlaskApp()
    my_app.start()