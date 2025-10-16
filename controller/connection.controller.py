"""
Connection Controller
"""
from flask import request, jsonify
from services.connection.service import ConnectionService

class ConnectionController:
    """Handle connection-related endpoints"""
    
    @staticmethod
    def send_request(session, user_id):
        """Send a connection request"""
        try:
            data = request.get_json()
            
            if 'addressee_id' not in data:
                return jsonify({'error': 'Addressee ID is required'}), 400
            
            addressee_id = data['addressee_id']
            message = data.get('message')
            
            if user_id == addressee_id:
                return jsonify({'error': 'Cannot connect with yourself'}), 400
            
            connection = ConnectionService.send_connection_request(
                session, user_id, addressee_id, message
            )
            
            if not connection:
                return jsonify({'error': 'Connection already exists'}), 409
            
            return jsonify({
                'message': 'Connection request sent',
                'connection': connection.to_dict()
            }), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def accept_request(session, user_id, connection_id):
        """Accept a connection request"""
        try:
            success = ConnectionService.accept_connection_request(session, connection_id, user_id)
            if not success:
                return jsonify({'error': 'Connection request not found'}), 404
            
            return jsonify({'message': 'Connection request accepted'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def reject_request(session, user_id, connection_id):
        """Reject a connection request"""
        try:
            success = ConnectionService.reject_connection_request(session, connection_id, user_id)
            if not success:
                return jsonify({'error': 'Connection request not found'}), 404
            
            return jsonify({'message': 'Connection request rejected'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_connections(session, user_id):
        """Get user's connections"""
        try:
            connections = ConnectionService.get_user_connections(session, user_id)
            
            return jsonify({
                'connections': [conn.to_dict() for conn in connections],
                'count': len(connections)
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @staticmethod
    def get_pending_requests(session, user_id):
        """Get pending connection requests"""
        try:
            requests = ConnectionService.get_pending_requests(session, user_id)
            
            return jsonify({
                'requests': [req.to_dict() for req in requests],
                'count': len(requests)
            }), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500
