from flask import Blueprint 

from src.auth.services.auth import AuthService

class AuthController:
    def __init__(self):
        self.authBp = Blueprint("auth", __name__)
        self.setupRoutes()

    def setupRoutes(self):
        @self.authBp.get("/me")
        def me():
            return AuthService.me()
        
        @self.authBp.post('/login')
        def login():
            return AuthService.login()