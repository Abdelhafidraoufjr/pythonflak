"""
Post routes
"""
from flask import Blueprint
from controller.post.controller import PostController
from routes.middleware import auth_required

def create_post_routes(get_session):
    """Create post routes"""
    post_bp = Blueprint('post', __name__, url_prefix='/api/posts')
    
    @post_bp.route('/', methods=['POST'])
    @auth_required
    def create_post(user_id):
        session = get_session()
        return PostController.create_post(session, user_id)
    
    @post_bp.route('/<int:post_id>', methods=['GET'])
    @auth_required
    def get_post(user_id, post_id):
        session = get_session()
        return PostController.get_post(session, post_id)
    
    @post_bp.route('/<int:post_id>', methods=['DELETE'])
    @auth_required
    def delete_post(user_id, post_id):
        session = get_session()
        return PostController.delete_post(session, user_id, post_id)
    
    @post_bp.route('/<int:post_id>/like', methods=['POST'])
    @auth_required
    def like_post(user_id, post_id):
        session = get_session()
        return PostController.like_post(session, post_id)
    
    @post_bp.route('/feed', methods=['GET'])
    @auth_required
    def get_feed(user_id):
        session = get_session()
        return PostController.get_feed(session, user_id)
    
    @post_bp.route('/user/<int:target_user_id>', methods=['GET'])
    @auth_required
    def get_user_posts(user_id, target_user_id):
        session = get_session()
        return PostController.get_user_posts(session, target_user_id)
    
    return post_bp
