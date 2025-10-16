"""
User routes
"""
from flask import Blueprint
from controller.user.controller import UserController
from routes.middleware import auth_required

def create_user_routes(get_session):
    """Create user routes"""
    user_bp = Blueprint('user', __name__, url_prefix='/api/users')
    
    @user_bp.route('/me', methods=['GET'])
    @auth_required
    def get_my_profile(user_id):
        session = get_session()
        return UserController.get_profile(session, user_id)
    
    @user_bp.route('/me', methods=['PUT'])
    @auth_required
    def update_my_profile(user_id):
        session = get_session()
        return UserController.update_profile(session, user_id)
    
    @user_bp.route('/search', methods=['GET'])
    @auth_required
    def search_users(user_id):
        session = get_session()
        return UserController.search_users(session)
    
    @user_bp.route('/<int:target_user_id>', methods=['GET'])
    @auth_required
    def get_user_profile(user_id, target_user_id):
        session = get_session()
        return UserController.get_user_by_id(session, target_user_id)
    
    return user_bp
