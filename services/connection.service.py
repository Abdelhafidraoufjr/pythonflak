"""
Connection Service for managing user connections
"""
from sqlalchemy.orm import Session
from model.connections.model import Connection, ConnectionStatus
from model.users.model import User
from datetime import datetime

class ConnectionService:
    """Handle connection-related business logic"""
    
    @staticmethod
    def send_connection_request(session: Session, requester_id: int, addressee_id: int, message: str = None) -> Connection:
        """Send a connection request"""
        # Check if connection already exists
        existing = session.query(Connection).filter(
            ((Connection.requester_id == requester_id) & (Connection.addressee_id == addressee_id)) |
            ((Connection.requester_id == addressee_id) & (Connection.addressee_id == requester_id))
        ).first()
        
        if existing:
            return None  # Connection already exists
        
        connection = Connection(
            requester_id=requester_id,
            addressee_id=addressee_id,
            message=message,
            status=ConnectionStatus.PENDING
        )
        
        session.add(connection)
        session.commit()
        session.refresh(connection)
        return connection
    
    @staticmethod
    def accept_connection_request(session: Session, connection_id: int, user_id: int) -> bool:
        """Accept a connection request"""
        connection = session.query(Connection).filter(
            Connection.id == connection_id,
            Connection.addressee_id == user_id,
            Connection.status == ConnectionStatus.PENDING
        ).first()
        
        if connection:
            connection.status = ConnectionStatus.ACCEPTED
            connection.responded_at = datetime.utcnow()
            
            # Update connection counts for both users
            requester = session.query(User).filter(User.id == connection.requester_id).first()
            addressee = session.query(User).filter(User.id == connection.addressee_id).first()
            
            if requester:
                requester.connections_count += 1
            if addressee:
                addressee.connections_count += 1
            
            session.commit()
            return True
        return False
    
    @staticmethod
    def reject_connection_request(session: Session, connection_id: int, user_id: int) -> bool:
        """Reject a connection request"""
        connection = session.query(Connection).filter(
            Connection.id == connection_id,
            Connection.addressee_id == user_id,
            Connection.status == ConnectionStatus.PENDING
        ).first()
        
        if connection:
            connection.status = ConnectionStatus.REJECTED
            connection.responded_at = datetime.utcnow()
            session.commit()
            return True
        return False
    
    @staticmethod
    def get_user_connections(session: Session, user_id: int):
        """Get all accepted connections for a user"""
        return session.query(Connection).filter(
            ((Connection.requester_id == user_id) | (Connection.addressee_id == user_id)),
            Connection.status == ConnectionStatus.ACCEPTED
        ).all()
    
    @staticmethod
    def get_pending_requests(session: Session, user_id: int):
        """Get pending connection requests received by user"""
        return session.query(Connection).filter(
            Connection.addressee_id == user_id,
            Connection.status == ConnectionStatus.PENDING
        ).all()
