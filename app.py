from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os
import secrets

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', secrets.token_hex(32))
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///portfolio.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SERVER_NAME'] = os.environ.get('SERVER_NAME', None)
app.config['PREFERRED_URL_SCHEME'] = os.environ.get('PREFERRED_URL_SCHEME', 'https')

db = SQLAlchemy(app)

# Security headers
@app.after_request
def after_request(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response

# Blog Post Model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    
    def __repr__(self):
        return f"BlogPost('{self.title}', '{self.date_posted}')"

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('index.html', posts=[]), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('index.html', posts=[]), 500

# Routes
@app.route('/')
def home():
    try:
        posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).limit(3).all()
    except Exception as e:
        posts = []
        flash('Unable to load recent posts', 'warning')
    return render_template('index.html', posts=posts)

@app.route('/old-home')
def old_home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/blog')
def blog():
    try:
        posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    except Exception as e:
        posts = []
        flash('Unable to load blog posts', 'warning')
    return render_template('blog.html', posts=posts)

@app.route('/blog/new', methods=['GET', 'POST'])
def new_blog_post():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        
        if title and content:
            try:
                post = BlogPost(title=title, content=content)
                db.session.add(post)
                db.session.commit()
                flash('Blog post created successfully!', 'success')
                return redirect(url_for('blog'))
            except Exception as e:
                db.session.rollback()
                flash('Error creating blog post. Please try again.', 'error')
        else:
            flash('Please fill in all fields', 'error')
    
    return render_template('new_post.html')

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('blog_post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

def create_tables():
    """Create database tables if they don't exist"""
    try:
        with app.app_context():
            db.create_all()
    except Exception as e:
        print(f"Error creating database tables: {e}")

if __name__ == '__main__':
    create_tables()
    # Use environment variables for debug mode in production
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 8000))
    print("🌐 Portfolio website starting...")
    print(f"📱 Local access: http://localhost:{port}")
    print("🔍 To find your network IP:")
    print("   - Mac: System Preferences → Network → Advanced → TCP/IP")
    print("   - Windows: Run 'ipconfig' in Command Prompt") 
    print(f"📶 Network access: http://YOUR_IP_ADDRESS:{port}")
    print("=" * 50)
    app.run(debug=debug_mode, host='0.0.0.0', port=port)