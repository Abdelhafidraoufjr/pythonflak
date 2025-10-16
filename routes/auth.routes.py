"""
Authentication routes
"""
from flask import Blueprint
from controller.auth.controller import AuthController

def create_auth_routes(get_session):
    """Create authentication routes"""
    auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')
    
    @auth_bp.route('/register', methods=['POST'])
    def register():
        session = get_session()
        return AuthController.register(session)
    
    @auth_bp.route('/login', methods=['POST'])
    def login():
        session = get_session()
        return AuthController.login(session)
    
    return auth_bp
