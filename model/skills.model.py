"""
Skills model for user skills and endorsements
"""
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from .base import Base, TimestampMixin

# Association table for user skills
user_skills = Table(
    'user_skills',
    Base.metadata,
    Column('user_id', Integer, ForeignKey('users.id', ondelete='CASCADE'), primary_key=True),
    Column('skill_id', Integer, ForeignKey('skills.id', ondelete='CASCADE'), primary_key=True),
    Column('endorsements_count', Integer, default=0)
)

class Skill(Base, TimestampMixin):
    """
    Skills that users can add to their profiles
    """
    __tablename__ = 'skills'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False, index=True)
    category = Column(String(100))  # e.g., "Programming", "Marketing", "Design"
    
    def __repr__(self):
        return f"<Skill(id={self.id}, name='{self.name}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }
