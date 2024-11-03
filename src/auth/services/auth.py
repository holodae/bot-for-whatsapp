from flask import request 

class AuthService:
    @staticmethod
    def me():
        return 'info'
    
    @staticmethod
    def login():
        req = request.json
        print(req)
        return ''