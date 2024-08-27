import datetime
from flask import Blueprint, request, session, jsonify
from flask_login import  login_user, login_required, current_user
from model.userModel import User
from werkzeug.security import generate_password_hash
from app import db


user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/api/user/login", methods=["POST"])
def login():
    username = request.json.get("username")  
    password = request.json.get("password")

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        return jsonify({"message": "Login successful", "token": "your-token-here", "success": True}), 200
    else:
        return jsonify({"message": "Invalid username or password", "success": False}), 401

    

# @user_bp.route("/api/user/register", methods=["POST"])
# def register():
#     data = request.get_json()
    
#     # Ensure the password is provided
#     password = data.get('password')
#     if not password:
#         return jsonify({'error': 'Password is required'}), 400

#     # Hash the password
#     password_hash = generate_password_hash(password, method="pbkdf2:sha256")

#     # Example: Collect other user data (username, email, etc.)
#     username = data.get('username')
#     email = data.get('email')

#     # Add your logic to store the user information in the database
#     # For example:
#     new_user = User(username=username, email=email, password_hash=password_hash)
#     db.session.add(new_user)
#     db.session.commit()

#     # Return a success message
#     return jsonify({'message': 'User registered successfully'}), 201


        
