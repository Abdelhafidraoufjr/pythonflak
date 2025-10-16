"""
Post Service for managing posts and feed
"""
from sqlalchemy.orm import Session
from model.posts.model import Post, PostType
from model.users.model import User
from datetime import datetime

class PostService:
    """Handle post-related business logic"""
    
    @staticmethod
    def create_post(session: Session, user_id: int, post_data: dict) -> Post:
        """Create a new post"""
        post = Post(
            user_id=user_id,
            content=post_data['content'],
            post_type=PostType[post_data.get('post_type', 'TEXT').upper()],
            media_url=post_data.get('media_url'),
            article_title=post_data.get('article_title'),
            article_link=post_data.get('article_link'),
            is_public=post_data.get('is_public', True)
        )
        
        session.add(post)
        session.commit()
        session.refresh(post)
        return post
    
    @staticmethod
    def get_post_by_id(session: Session, post_id: int) -> Post:
        """Get post by ID"""
        return session.query(Post).filter(Post.id == post_id).first()
    
    @staticmethod
    def get_user_posts(session: Session, user_id: int, limit: int = 20, offset: int = 0):
        """Get posts by a specific user"""
        return session.query(Post).filter(
            Post.user_id == user_id
        ).order_by(Post.created_at.desc()).limit(limit).offset(offset).all()
    
    @staticmethod
    def get_feed(session: Session, user_id: int, limit: int = 20, offset: int = 0):
        """Get personalized feed for user (simplified - would include connections' posts)"""
        return session.query(Post).filter(
            Post.is_public == True
        ).order_by(Post.created_at.desc()).limit(limit).offset(offset).all()
    
    @staticmethod
    def delete_post(session: Session, post_id: int, user_id: int) -> bool:
        """Delete a post"""
        post = session.query(Post).filter(
            Post.id == post_id,
            Post.user_id == user_id
        ).first()
        
        if post:
            session.delete(post)
            session.commit()
            return True
        return False
    
    @staticmethod
    def increment_likes(session: Session, post_id: int):
        """Increment post likes count"""
        post = session.query(Post).filter(Post.id == post_id).first()
        if post:
            post.likes_count += 1
            session.commit()
    
    @staticmethod
    def increment_views(session: Session, post_id: int):
        """Increment post views count"""
        post = session.query(Post).filter(Post.id == post_id).first()
        if post:
            post.views_count += 1
            session.commit()
