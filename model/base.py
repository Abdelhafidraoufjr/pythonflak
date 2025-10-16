"""
Base model configuration
"""
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, DateTime

Base = declarative_base()

class TimestampMixin:
    """Mixin to add timestamp fields to models"""
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
