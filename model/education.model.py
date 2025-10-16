"""
Education model for academic history
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Date
from .base import Base, TimestampMixin

class Education(Base, TimestampMixin):
    """
    Education history
    """
    __tablename__ = 'education'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Institution Information
    school = Column(String(255), nullable=False)
    degree = Column(String(255))  # Bachelor's, Master's, PhD, etc.
    field_of_study = Column(String(255))
    
    # Duration
    start_date = Column(Date)
    end_date = Column(Date)
    
    # Additional Info
    grade = Column(String(50))
    activities = Column(Text)  # Extracurricular activities
    description = Column(Text)
    
    def __repr__(self):
        return f"<Education(id={self.id}, school='{self.school}', degree='{self.degree}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'school': self.school,
            'degree': self.degree,
            'field_of_study': self.field_of_study,
            'start_date': self.start_date.isoformat() if self.start_date else None,
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'grade': self.grade,
            'activities': self.activities,
            'description': self.description
        }
