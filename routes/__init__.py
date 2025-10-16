"""
Routes package - Register all routes
"""
from routes.auth.routes import create_auth_routes
from routes.user.routes import create_user_routes
from routes.post.routes import create_post_routes
from routes.connection.routes import create_connection_routes

def register_routes(app, get_session):
    """Register all application routes"""
    
    # Register blueprints
    app.register_blueprint(create_auth_routes(get_session))
    app.register_blueprint(create_user_routes(get_session))
    app.register_blueprint(create_post_routes(get_session))
    app.register_blueprint(create_connection_routes(get_session))
    
    print("✓ All routes registered successfully")
