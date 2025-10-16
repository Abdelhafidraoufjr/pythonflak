"""
User Service for business logic
"""
from sqlalchemy.orm import Session
from model.users.model import User
from services.auth.service import AuthService
from datetime import datetime

class UserService:
    """Handle user-related business logic"""
    
    @staticmethod
    def create_user(session: Session, user_data: dict) -> User:
        """Create a new user"""
        # Hash password
        password_hash = AuthService.hash_password(user_data['password'])
        
        # Create user
        user = User(
            email=user_data['email'],
            password_hash=password_hash,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            headline=user_data.get('headline'),
            location=user_data.get('location'),
            industry=user_data.get('industry')
        )
        
        session.add(user)
        session.commit()
        session.refresh(user)
        return user
    
    @staticmethod
    def get_user_by_id(session: Session, user_id: int) -> User:
        """Get user by ID"""
        return session.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(session: Session, email: str) -> User:
        """Get user by email"""
        return session.query(User).filter(User.email == email).first()
    
    @staticmethod
    def update_user(session: Session, user_id: int, update_data: dict) -> User:
        """Update user information"""
        user = session.query(User).filter(User.id == user_id).first()
        if not user:
            return None
        
        for key, value in update_data.items():
            if hasattr(user, key) and key not in ['id', 'password_hash', 'created_at']:
                setattr(user, key, value)
        
        session.commit()
        session.refresh(user)
        return user
    
    @staticmethod
    def update_last_login(session: Session, user_id: int):
        """Update user's last login timestamp"""
        user = session.query(User).filter(User.id == user_id).first()
        if user:
            user.last_login = datetime.utcnow()
            session.commit()
    
    @staticmethod
    def search_users(session: Session, query: str, limit: int = 20):
        """Search users by name or headline"""
        search_pattern = f"%{query}%"
        return session.query(User).filter(
            (User.first_name.ilike(search_pattern)) |
            (User.last_name.ilike(search_pattern)) |
            (User.headline.ilike(search_pattern))
        ).limit(limit).all()
