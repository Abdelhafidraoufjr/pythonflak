"""
Jobs model for job postings
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, DateTime, Float
from datetime import datetime
import enum
from .base import Base, TimestampMixin

class JobType(enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    INTERNSHIP = "internship"
    FREELANCE = "freelance"

class ExperienceLevel(enum.Enum):
    ENTRY = "entry"
    INTERMEDIATE = "intermediate"
    SENIOR = "senior"
    EXECUTIVE = "executive"

class Job(Base, TimestampMixin):
    """
    Job postings
    """
    __tablename__ = 'jobs'
    
    id = Column(Integer, primary_key=True, index=True)
    posted_by = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Job Details
    title = Column(String(255), nullable=False, index=True)
    company = Column(String(255), nullable=False)
    company_logo = Column(String(500))
    location = Column(String(255))
    is_remote = Column(Boolean, default=False)
    
    # Job Type
    job_type = Column(Enum(JobType), nullable=False)
    experience_level = Column(Enum(ExperienceLevel))
    
    # Description
    description = Column(Text, nullable=False)
    requirements = Column(Text)
    responsibilities = Column(Text)
    
    # Compensation
    salary_min = Column(Float)
    salary_max = Column(Float)
    salary_currency = Column(String(10), default='USD')
    
    # Skills
    required_skills = Column(Text)  # JSON or comma-separated
    
    # Application
    application_url = Column(String(500))
    application_email = Column(String(255))
    
    # Status
    is_active = Column(Boolean, default=True)
    deadline = Column(DateTime)
    
    # Stats
    applications_count = Column(Integer, default=0)
    views_count = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Job(id={self.id}, title='{self.title}', company='{self.company}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'posted_by': self.posted_by,
            'title': self.title,
            'company': self.company,
            'location': self.location,
            'is_remote': self.is_remote,
            'job_type': self.job_type.value if self.job_type else None,
            'experience_level': self.experience_level.value if self.experience_level else None,
            'description': self.description,
            'salary_min': self.salary_min,
            'salary_max': self.salary_max,
            'salary_currency': self.salary_currency,
            'is_active': self.is_active,
            'applications_count': self.applications_count,
            'views_count': self.views_count,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
