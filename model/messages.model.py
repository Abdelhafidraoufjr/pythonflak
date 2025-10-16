"""
Messages model for direct messaging
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean, DateTime
from datetime import datetime
from .base import Base

class Message(Base):
    """
    Direct messages between users
    """
    __tablename__ = 'messages'
    
    id = Column(Integer, primary_key=True, index=True)
    
    # Sender and Receiver
    sender_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    receiver_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Message content
    content = Column(Text, nullable=False)
    
    # Attachment
    attachment_url = Column(String(500))
    attachment_type = Column(String(50))  # image, document, etc.
    
    # Status
    is_read = Column(Boolean, default=False)
    read_at = Column(DateTime)
    
    # Timestamps
    sent_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self):
        return f"<Message(id={self.id}, from={self.sender_id}, to={self.receiver_id})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'content': self.content,
            'attachment_url': self.attachment_url,
            'is_read': self.is_read,
            'read_at': self.read_at.isoformat() if self.read_at else None,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None
        }
