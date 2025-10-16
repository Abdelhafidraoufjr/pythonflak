"""
Comments model for post comments
"""
from sqlalchemy import Column, Integer, Text, ForeignKey
from .base import Base, TimestampMixin

class Comment(Base, TimestampMixin):
    """
    Comments on posts
    """
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey('posts.id', ondelete='CASCADE'), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Comment content
    content = Column(Text, nullable=False)
    
    # Nested comments (replies)
    parent_comment_id = Column(Integer, ForeignKey('comments.id', ondelete='CASCADE'))
    
    # Engagement
    likes_count = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Comment(id={self.id}, post_id={self.post_id}, user_id={self.user_id})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'post_id': self.post_id,
            'user_id': self.user_id,
            'content': self.content,
            'parent_comment_id': self.parent_comment_id,
            'likes_count': self.likes_count,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
