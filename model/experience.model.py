"""
Experience model for work history
"""
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from .base import Base, TimestampMixin

class Experience(Base, TimestampMixin):
    """
    Professional experience/work history
    """
    __tablename__ = 'experiences'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Job Information
    title = Column(String(255), nullable=False)  # Job title
    employment_type = Column(String(50))  # Full-time, Part-time, Contract, etc.
    company_name = Column(String(255), nullable=False)
    company_logo = Column(String(500))  # URL to company logo
    location = Column(String(255))
    
    # Duration
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)  # Null if currently working
    is_current = Column(Boolean, default=False)
    
    # Description
    description = Column(Text)
    
    # Skills used in this role
    skills = Column(Text)  # Comma-separated or JSON
    
    def __repr__(self):
        return f"<Experience(id={self.id}, title='{self.title}', company='{self.company_name}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'title': self.title,
            'employment_type': self.employment_type,
            'company_name': self.company_name,
            'location': self.location,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'is_current': self.is_current,
            'description': self.description,
            'skills': self.skills
        }
