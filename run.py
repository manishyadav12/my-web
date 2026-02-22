#!/usr/bin/env python3
"""
Portfolio Website Launcher
Simple script to start the Flask development server with proper configuration.
"""

import os
import sys
from app import app, db

def setup_database():
    """Initialize the database with tables"""
    with app.app_context():
        db.create_all()
        print("✅ Database initialized successfully!")

def main():
    """Main function to run the portfolio website"""
    print("🚀 Starting Manish Yadav's Portfolio Website...")
    print("=" * 50)
    
    # Check if virtual environment is activated
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Virtual environment detected")
    else:
        print("⚠️  No virtual environment detected. Consider using one for better dependency management.")
    
    # Setup database
    setup_database()
    
    # Start the Flask development server
    print("\n🌟 Portfolio website is starting...")
    print("📱 Access your portfolio at: http://localhost:5000")
    print("🛑 Press Ctrl+C to stop the server")
    print("=" * 50)
    
    try:
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            use_reloader=True
        )
    except KeyboardInterrupt:
        print("\n👋 Portfolio website stopped. Thanks for visiting!")
    except Exception as e:
        print(f"\n❌ Error starting the website: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()