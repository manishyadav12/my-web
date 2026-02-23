#!/usr/bin/env python3
"""
Simple startup script for Render deployment
"""
import os
import subprocess
import sys

def main():
    # Get port from environment variable
    port = os.environ.get('PORT', '8000')
    
    print(f"🚀 Starting portfolio website on port {port}")
    print(f"📊 Environment: {'Production' if os.environ.get('RENDER') else 'Development'}")
    
    # Gunicorn command with explicit port binding
    cmd = [
        'gunicorn',
        'app:app',
        '--bind', f'0.0.0.0:{port}',
        '--workers', '1',
        '--timeout', '120',
        '--access-logfile', '-',
        '--error-logfile', '-',
        '--log-level', 'info'
    ]
    
    print(f"🔧 Command: {' '.join(cmd)}")
    
    try:
        # Execute gunicorn
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to start server: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print("🛑 Server stopped by user")
        sys.exit(0)

if __name__ == '__main__':
    main()