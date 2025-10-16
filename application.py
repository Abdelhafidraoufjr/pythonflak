"""
Main Flask Application Entry Point - LinkedIn-like Backend
This module initializes the Flask application with database connection
and configures all necessary components.
"""

import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from config.database_config import DatabaseConfig
from model.base import Base
from routes import register_routes

# Load environment variables
load_dotenv()

# Initialize Flask App
app = Flask(__name__)

# Enable CORS
CORS(app, resources={
    r"/api/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Configure Flask
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_ECHO'] = False

def init_database():
    """
    Initialize database connection and create engine with optimized settings.
    """
    try:
        db_url = DatabaseConfig.get_db_url()
        engine_options = DatabaseConfig.get_engine_options()
        
        # Create SQLAlchemy engine
        engine = create_engine(db_url, **engine_options)
        
        # Test database connection
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        
        print("✓ Database connection successful!")
        print(f"✓ Connected to: {DatabaseConfig.DB_NAME} at {DatabaseConfig.DB_HOST}:{DatabaseConfig.DB_PORT}")
        
        # Create all tables
        Base.metadata.create_all(engine)
        print("✓ Database tables created/verified successfully!")
        
        # Create session factory
        Session = scoped_session(sessionmaker(bind=engine))
        return engine, Session
    
    except Exception as e:
        print(f"✗ Database connection failed: {str(e)}")
        raise

# Initialize database
try:
    db_engine, Session = init_database()
    app.db_engine = db_engine
    app.Session = Session
except Exception as e:
    print(f"Failed to initialize database: {str(e)}")
    raise

# Helper function to get session
def get_session():
    """Get database session"""
    return Session()

# Register all routes
register_routes(app, get_session)

# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'LinkedIn-like Backend is running',
        'database': 'connected',
        'version': '1.0.0'
    }), 200

# API Info endpoint
@app.route('/api', methods=['GET'])
def api_info():
    """API information endpoint"""
    return jsonify({
        'name': 'LinkedIn-like Backend API',
        'version': '1.0.0',
        'endpoints': {
            'auth': {
                'register': 'POST /api/auth/register',
                'login': 'POST /api/auth/login'
            },
            'users': {
                'get_profile': 'GET /api/users/me',
                'update_profile': 'PUT /api/users/me',
                'search': 'GET /api/users/search',
                'get_user': 'GET /api/users/:id'
            },
            'posts': {
                'create': 'POST /api/posts/',
                'get': 'GET /api/posts/:id',
                'delete': 'DELETE /api/posts/:id',
                'like': 'POST /api/posts/:id/like',
                'feed': 'GET /api/posts/feed',
                'user_posts': 'GET /api/posts/user/:id'
            },
            'connections': {
                'send_request': 'POST /api/connections/request',
                'accept': 'POST /api/connections/:id/accept',
                'reject': 'POST /api/connections/:id/reject',
                'my_connections': 'GET /api/connections/my-connections',
                'pending': 'GET /api/connections/pending'
            }
        }
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Shutdown handler
@app.teardown_appcontext
def shutdown_session(exception=None):
    """Close database session on app shutdown"""
    Session.remove()

if __name__ == '__main__':
    print("\n" + "="*60)
    print("Starting LinkedIn-like Backend Server")
    print("="*60 + "\n")
    
    # Run the application
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('FLASK_PORT', 5000)),
        debug=os.getenv('FLASK_ENV', 'development') == 'development'
    )
