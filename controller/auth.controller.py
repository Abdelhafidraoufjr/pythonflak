"""
Authentication Controller
"""
from flask import request, jsonify
from services.auth.service import AuthService
from services.user.service import UserService

class AuthController:
    """Handle authentication endpoints"""
    
    @staticmethod
    def register(session):
        """Register a new user"""
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['email', 'password', 'first_name', 'last_name']
            if not all(field in data for field in required_fields):
                return jsonify({'error': 'Missing required fields'}), 400
            
            # Check if user already exists
            existing_user = UserService.get_user_by_email(session, data['email'])
            if existing_user:
                return jsonify({'error': 'Email already registered'}), 409
            
            # Create user
            user = UserService.create_user(session, data)
            
            # Generate token
            token = AuthService.generate_token(user.id, user.email)
            
            return jsonify({
                'message': 'User registered successfully',
                'user': user.to_dict(),
                'token': token
            }), 201
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def login(session):
        """Login user"""
        try:
            data = request.get_json()
            
            # Validate required fields
            if 'email' not in data or 'password' not in data:
                return jsonify({'error': 'Email and password are required'}), 400
            
            # Get user
            user = UserService.get_user_by_email(session, data['email'])
            if not user:
                return jsonify({'error': 'Invalid email or password'}), 401
            
            # Verify password
            if not AuthService.verify_password(data['password'], user.password_hash):
                return jsonify({'error': 'Invalid email or password'}), 401
            
            # Update last login
            UserService.update_last_login(session, user.id)
            
            # Generate token
            token = AuthService.generate_token(user.id, user.email)
            
            return jsonify({
                'message': 'Login successful',
                'user': user.to_dict(),
                'token': token
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
