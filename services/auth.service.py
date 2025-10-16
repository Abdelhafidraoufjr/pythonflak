"""
Authentication Service
"""
from flask_bcrypt import Bcrypt
from datetime import datetime, timedelta
import jwt
import os

bcrypt = Bcrypt()

class AuthService:
    """Handle authentication operations"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Hash a password"""
        return bcrypt.generate_password_hash(password).decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, password_hash: str) -> bool:
        """Verify a password against its hash"""
        return bcrypt.check_password_hash(password_hash, password)
    
    @staticmethod
    def generate_token(user_id: int, email: str) -> str:
        """Generate JWT token"""
        payload = {
            'user_id': user_id,
            'email': email,
            'exp': datetime.utcnow() + timedelta(days=7),
            'iat': datetime.utcnow()
        }
        secret_key = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
        return jwt.encode(payload, secret_key, algorithm='HS256')
    
    @staticmethod
    def verify_token(token: str) -> dict:
        """Verify JWT token and return payload"""
        try:
            secret_key = os.getenv('JWT_SECRET_KEY', 'your-secret-key-change-in-production')
            payload = jwt.decode(token, secret_key, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
