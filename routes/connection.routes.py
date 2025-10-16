"""
Connection routes
"""
from flask import Blueprint
from controller.connection.controller import ConnectionController
from routes.middleware import auth_required

def create_connection_routes(get_session):
    """Create connection routes"""
    connection_bp = Blueprint('connection', __name__, url_prefix='/api/connections')
    
    @connection_bp.route('/request', methods=['POST'])
    @auth_required
    def send_request(user_id):
        session = get_session()
        return ConnectionController.send_request(session, user_id)
    
    @connection_bp.route('/<int:connection_id>/accept', methods=['POST'])
    @auth_required
    def accept_request(user_id, connection_id):
        session = get_session()
        return ConnectionController.accept_request(session, user_id, connection_id)
    
    @connection_bp.route('/<int:connection_id>/reject', methods=['POST'])
    @auth_required
    def reject_request(user_id, connection_id):
        session = get_session()
        return ConnectionController.reject_request(session, user_id, connection_id)
    
    @connection_bp.route('/my-connections', methods=['GET'])
    @auth_required
    def get_connections(user_id):
        session = get_session()
        return ConnectionController.get_connections(session, user_id)
    
    @connection_bp.route('/pending', methods=['GET'])
    @auth_required
    def get_pending_requests(user_id):
        session = get_session()
        return ConnectionController.get_pending_requests(session, user_id)
    
    return connection_bp
