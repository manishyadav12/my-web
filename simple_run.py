#!/usr/bin/env python3
"""
Simple Portfolio Website Runner
Runs the website with minimal dependencies - good for quick testing
"""

import sys
import subprocess
import os

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required")
        print(f"Your version: {sys.version}")
        return False
    return True

def install_dependencies():
    """Try to install dependencies using pip"""
    print("📦 Installing required packages...")
    
    packages = [
        "Flask>=2.0.0",
        "Flask-SQLAlchemy>=3.0.0"
    ]
    
    for package in packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "--user", package
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError:
            print(f"⚠️  Could not install {package}")
            print("Please install Flask manually: pip install Flask Flask-SQLAlchemy")
            return False
    
    print("✅ Dependencies installed!")
    return True

def setup_and_run():
    """Setup the database and run the application"""
    try:
        # Import after potential installation
        from app import app, db
        
        print("🔧 Setting up database...")
        with app.app_context():
            db.create_all()
        print("✅ Database ready!")
        
        print("\n🌟 Starting Portfolio Website...")
        print("📱 Open your browser and visit: http://localhost:5000")
        print("🛑 Press Ctrl+C to stop")
        print("=" * 50)
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except ImportError as e:
        print(f"❌ Missing dependencies: {e}")
        print("Please install Flask: pip install Flask Flask-SQLAlchemy")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False
    
    return True

def main():
    """Main function"""
    print("🚀 Manish Yadav - Portfolio Website")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Try to import Flask first
    try:
        import flask
        import flask_sqlalchemy
        print("✅ Dependencies already available!")
    except ImportError:
        print("📦 Flask not found, attempting to install...")
        if not install_dependencies():
            print("\n💡 Manual Installation Instructions:")
            print("1. pip install Flask Flask-SQLAlchemy")
            print("2. python simple_run.py")
            sys.exit(1)
    
    # Setup and run
    if not setup_and_run():
        sys.exit(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Portfolio website stopped!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)