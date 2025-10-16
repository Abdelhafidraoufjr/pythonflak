"""
User model for LinkedIn-like application
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Enum
from datetime import datetime
import enum
from .base import Base, TimestampMixin

class UserRole(enum.Enum):
    USER = "user"
    RECRUITER = "recruiter"
    ADMIN = "admin"

class User(Base, TimestampMixin):
    """
    User model representing a professional user in the LinkedIn-like application
    """
    __tablename__ = 'users'
    
    # Primary Key
    id = Column(Integer, primary_key=True, index=True)
    
    # Authentication
    email = Column(String(255), unique=True, nullable=False, index=True)
    password_hash = Column(String(255), nullable=False)
    
    # Personal Information
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    headline = Column(String(255))  # Professional headline (e.g., "Software Engineer at Google")
    about = Column(Text)  # About/Summary section
    
    # Profile
    profile_picture = Column(String(500))  # URL to profile picture
    cover_photo = Column(String(500))  # URL to cover photo
    location = Column(String(255))
    industry = Column(String(100))
    
    # Contact
    phone = Column(String(20))
    website = Column(String(255))
    
    # Professional
    current_position = Column(String(255))
    company = Column(String(255))
    
    # Account Status
    is_active = Column(Boolean, default=True)
    is_verified = Column(Boolean, default=False)
    is_premium = Column(Boolean, default=False)
    role = Column(Enum(UserRole), default=UserRole.USER)
    
    # Profile Stats
    connections_count = Column(Integer, default=0)
    followers_count = Column(Integer, default=0)
    profile_views = Column(Integer, default=0)
    
    # Timestamps
    last_login = Column(DateTime)
    email_verified_at = Column(DateTime)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.first_name} {self.last_name}', email='{self.email}')>"
    
    def to_dict(self):
        """Convert user object to dictionary"""
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'headline': self.headline,
            'about': self.about,
            'profile_picture': self.profile_picture,
            'cover_photo': self.cover_photo,
            'location': self.location,
            'industry': self.industry,
            'current_position': self.current_position,
            'company': self.company,
            'is_verified': self.is_verified,
            'is_premium': self.is_premium,
            'connections_count': self.connections_count,
            'followers_count': self.followers_count,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }



