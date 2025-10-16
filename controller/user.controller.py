"""
User Controller
"""
from flask import request, jsonify
from services.user.service import UserService

class UserController:
    """Handle user-related endpoints"""
    
    @staticmethod
    def get_profile(session, user_id):
        """Get user profile"""
        try:
            user = UserService.get_user_by_id(session, user_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            
            return jsonify(user.to_dict()), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def update_profile(session, user_id):
        """Update user profile"""
        try:
            data = request.get_json()
            
            user = UserService.update_user(session, user_id, data)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            
            return jsonify({
                'message': 'Profile updated successfully',
                'user': user.to_dict()
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def search_users(session):
        """Search users"""
        try:
            query = request.args.get('q', '')
            limit = int(request.args.get('limit', 20))
            
            if not query:
                return jsonify({'error': 'Search query is required'}), 400
            
            users = UserService.search_users(session, query, limit)
            
            return jsonify({
                'results': [user.to_dict() for user in users],
                'count': len(users)
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_user_by_id(session, target_user_id):
        """Get another user's public profile"""
        try:
            user = UserService.get_user_by_id(session, target_user_id)
            if not user:
                return jsonify({'error': 'User not found'}), 404
            
            # Return public profile info
            profile_data = user.to_dict()
            # Remove sensitive information
            profile_data.pop('email', None)
            
            return jsonify(profile_data), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
