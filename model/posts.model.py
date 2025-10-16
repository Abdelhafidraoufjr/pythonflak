"""
Posts model for user posts/updates
"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean
import enum
from .base import Base, TimestampMixin

class PostType(enum.Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    ARTICLE = "article"
    POLL = "poll"

class Post(Base, TimestampMixin):
    """
    User posts/updates similar to LinkedIn feed
    """
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False, index=True)
    
    # Post Content
    content = Column(Text, nullable=False)
    post_type = Column(Enum(PostType), default=PostType.TEXT)
    
    # Media
    media_url = Column(String(500))  # Image/Video URL
    media_type = Column(String(50))  # image/jpeg, video/mp4, etc.
    
    # Article specific
    article_title = Column(String(255))
    article_link = Column(String(500))
    
    # Engagement
    likes_count = Column(Integer, default=0)
    comments_count = Column(Integer, default=0)
    shares_count = Column(Integer, default=0)
    views_count = Column(Integer, default=0)
    
    # Visibility
    is_public = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<Post(id={self.id}, user_id={self.user_id}, type='{self.post_type}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content,
            'post_type': self.post_type.value if self.post_type else None,
            'media_url': self.media_url,
            'article_title': self.article_title,
            'article_link': self.article_link,
            'likes_count': self.likes_count,
            'comments_count': self.comments_count,
            'shares_count': self.shares_count,
            'views_count': self.views_count,
            'is_public': self.is_public,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
