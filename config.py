"""
Configuration settings for the Portfolio Website
"""

import os
from datetime import timedelta

class Config:
    """Base configuration class"""
    
    # Basic Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///portfolio.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Application settings
    POSTS_PER_PAGE = 10
    
    # Security settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    
    # Email configuration (for contact forms)
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    
    # Personal information
    SITE_TITLE = "Manish Yadav - DevOps Engineer"
    SITE_DESCRIPTION = "Portfolio website showcasing DevOps and Cloud Engineering expertise"
    AUTHOR_NAME = "Manish Yadav"
    AUTHOR_EMAIL = "manish25102@gmail.com"
    AUTHOR_PHONE = "+91 7376356606"
    AUTHOR_LINKEDIN = "https://linkedin.com/in/manishyadav12"
    AUTHOR_GITHUB = "https://github.com/manishyadav"
    AUTHOR_LOCATION = "Bangalore, India"

class DevelopmentConfig(Config):
    """Development environment configuration"""
    DEBUG = True
    DEVELOPMENT = True
    
class ProductionConfig(Config):
    """Production environment configuration"""
    DEBUG = False
    DEVELOPMENT = False
    
    # Use stronger secret key in production
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-must-set-a-secret-key-in-production'

class TestingConfig(Config):
    """Testing environment configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}