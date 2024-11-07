from flask import Blueprint, request, jsonify
from ..services.user_service import UserService

class UserController:
    def __init__(self):
        self.user_bp = Blueprint('user_bp', __name__)
        self.setup_routes()

    def setup_routes(self):
        @self.user_bp.post("/add_user")
        def add_user():
            req = request.json
            new_user = UserService.add_user(req.get("username"), req.get("email"))
            return jsonify({'message': f'User {new_user.username} added!'}), 201

        @self.user_bp.get("/users")
        def list_users():
            users = UserService.get_all_users()
            return jsonify([{'username': user.username, 'email': user.email} for user in users])
