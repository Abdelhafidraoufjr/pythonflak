"""
Connections model for user relationships
"""
from sqlalchemy import Column, Integer, ForeignKey, Enum, DateTime, Text
from datetime import datetime
import enum
from .base import Base

class ConnectionStatus(enum.Enum):
    PENDING = "pending"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    BLOCKED = "blocked"

class Connection(Base):
    """
    User connections (similar to LinkedIn connections)
    """
    __tablename__ = 'connections'
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Connection parties
    requester_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    addressee_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Status
    status = Column(Enum(ConnectionStatus), default=ConnectionStatus.PENDING, nullable=False)
    
    # Optional message with connection request
    message = Column(Text)
    
    # Timestamps
    requested_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    responded_at = Column(DateTime)
    
    def __repr__(self):
        return f"<Connection(id={self.id}, from={self.requester_id}, to={self.addressee_id}, status='{self.status}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'requester_id': self.requester_id,
            'addressee_id': self.addressee_id,
            'status': self.status.value if self.status else None,
            'message': self.message,
            'requested_at': self.requested_at.isoformat() if self.requested_at else None,
            'responded_at': self.responded_at.isoformat() if self.responded_at else None
        }
