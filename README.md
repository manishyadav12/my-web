# Portfolio Website

A modern, minimalist portfolio website built with Flask featuring a dark theme, responsive design, and interactive elements.

## Features

- 🎨 Modern dark theme with gradient accents
- 📱 Fully responsive design
- ⚡ Single-page scrollable layout
- 📝 Blog functionality with SQLAlchemy
- 🚀 Production-ready with security headers
- 🌐 Easy deployment to cloud platforms

## Local Development

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)

### Installation

1. **Clone/Download the project**
2. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Access your website:**
   - Local: http://localhost:8000
   - Network: http://YOUR_IP:8000

## Deployment

### Deploy to Render (Recommended)

1. **Create GitHub repository and push code**
2. **Go to [render.com](https://render.com) and sign up**
3. **Create new Web Service from GitHub repo**
4. **Render will auto-detect Flask and deploy**

### Deploy to Railway

1. **Go to [railway.app](https://railway.app)**
2. **Connect GitHub repository**
3. **Deploy automatically**

### Deploy to PythonAnywhere

1. **Upload files to PythonAnywhere**
2. **Install dependencies in console**
3. **Configure WSGI application**

## Project Structure

```
my-portfolio/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── runtime.txt        # Python version for deployment
├── render.yaml        # Render deployment config
├── Procfile          # Process configuration
├── templates/        # HTML templates
│   ├── base.html     # Base template
│   └── index.html    # Main page
└── static/          # Static assets
    ├── css/
    │   └── style.css # Main stylesheet
    └── js/
        └── script.js # JavaScript functionality
```

## Technologies Used

- **Backend:** Python, Flask, SQLAlchemy
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite (development), PostgreSQL (production)
- **Deployment:** Render, Railway, PythonAnywhere
- **Icons:** Font Awesome 6.0

## Contact

- **Email:** manish25102@gmail.com
- **LinkedIn:** [linkedin.com/in/manishyadav12](https://linkedin.com/in/manishyadav12)
- **Phone:** +91 7376356606