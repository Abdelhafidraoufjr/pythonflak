"""
Models package - LinkedIn-like application
"""
# Import separately to avoid circular imports
from .base import Base, TimestampMixin

# Now we need to import from files with dots in names
# Python doesn't handle module names with dots well, so we'll use importlib
import importlib.util
import sys
from pathlib import Path

# Get the model directory
model_dir = Path(__file__).parent

# Helper function to import from files with dots
def import_from_dotted_file(filename, *names):
    module_path = model_dir / filename
    spec = importlib.util.spec_from_file_location(filename.replace('.py', ''), module_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return tuple(getattr(module, name) for name in names)

# Import all models
User, UserRole = import_from_dotted_file('users.model.py', 'User', 'UserRole')
Experience = import_from_dotted_file('experience.model.py', 'Experience')[0]
Education = import_from_dotted_file('education.model.py', 'Education')[0]
Skill, user_skills = import_from_dotted_file('skills.model.py', 'Skill', 'user_skills')
Post, PostType = import_from_dotted_file('posts.model.py', 'Post', 'PostType')
Connection, ConnectionStatus = import_from_dotted_file('connections.model.py', 'Connection', 'ConnectionStatus')
Comment = import_from_dotted_file('comments.model.py', 'Comment')[0]
Job, JobType, ExperienceLevel = import_from_dotted_file('jobs.model.py', 'Job', 'JobType', 'ExperienceLevel')
Message = import_from_dotted_file('messages.model.py', 'Message')[0]

__all__ = [
    'Base',
    'TimestampMixin',
    'User',
    'UserRole',
    'Experience',
    'Education',
    'Skill',
    'user_skills',
    'Post',
    'PostType',
    'Connection',
    'ConnectionStatus',
    'Comment',
    'Job',
    'JobType',
    'ExperienceLevel',
    'Message'
]
