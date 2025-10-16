"""
Post Controller
"""
from flask import request, jsonify
from services.post.service import PostService

class PostController:
    """Handle post-related endpoints"""
    
    @staticmethod
    def create_post(session, user_id):
        """Create a new post"""
        try:
            data = request.get_json()
            
            if 'content' not in data:
                return jsonify({'error': 'Content is required'}), 400
            
            post = PostService.create_post(session, user_id, data)
            
            return jsonify({
                'message': 'Post created successfully',
                'post': post.to_dict()
            }), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_post(session, post_id):
        """Get a specific post"""
        try:
            post = PostService.get_post_by_id(session, post_id)
            if not post:
                return jsonify({'error': 'Post not found'}), 404
            
            # Increment views
            PostService.increment_views(session, post_id)
            
            return jsonify(post.to_dict()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_user_posts(session, target_user_id):
        """Get posts by a specific user"""
        try:
            limit = int(request.args.get('limit', 20))
            offset = int(request.args.get('offset', 0))
            
            posts = PostService.get_user_posts(session, target_user_id, limit, offset)
            
            return jsonify({
                'posts': [post.to_dict() for post in posts],
                'count': len(posts)
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_feed(session, user_id):
        """Get personalized feed"""
        try:
            limit = int(request.args.get('limit', 20))
            offset = int(request.args.get('offset', 0))
            
            posts = PostService.get_feed(session, user_id, limit, offset)
            
            return jsonify({
                'posts': [post.to_dict() for post in posts],
                'count': len(posts)
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def delete_post(session, user_id, post_id):
        """Delete a post"""
        try:
            success = PostService.delete_post(session, post_id, user_id)
            if not success:
                return jsonify({'error': 'Post not found or unauthorized'}), 404
            
            return jsonify({'message': 'Post deleted successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def like_post(session, post_id):
        """Like a post"""
        try:
            PostService.increment_likes(session, post_id)
            return jsonify({'message': 'Post liked successfully'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
