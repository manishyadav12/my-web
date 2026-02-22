# Manish Yadav - Portfolio Website

A modern, minimalist, dark-themed portfolio website built with Flask, featuring a personal blog and showcasing professional experience in DevOps and Cloud Engineering.

## Features

- **Modern Dark UI**: Sleek, minimalist design with a professional dark theme
- **Responsive Design**: Fully responsive across all devices
- **Personal Blog**: Create, manage, and display blog posts
- **Professional Showcase**: Detailed experience, projects, and skills sections
- **Interactive Elements**: Smooth animations and transitions
- **Contact Integration**: Professional contact information and forms

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with CSS Grid and Flexbox
- **Icons**: Font Awesome
- **Fonts**: Google Fonts (Inter)

## Quick Start

1. **Clone or navigate to the project directory:**
   ```bash
   cd my-portfolio
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
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

5. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## Project Structure

```
my-portfolio/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # Jinja2 HTML templates
│   ├── base.html         # Base template with navigation
│   ├── home.html         # Homepage with hero section
│   ├── about.html        # About page with skills
│   ├── experience.html   # Professional experience timeline
│   ├── projects.html     # Featured projects showcase
│   ├── blog.html         # Blog listing page
│   ├── blog_post.html    # Individual blog post view
│   ├── new_post.html     # Blog post creation form
│   └── contact.html      # Contact information
└── static/               # Static assets
    ├── css/
    │   └── style.css     # Main stylesheet with dark theme
    └── js/
        └── script.js     # Interactive functionality
```

## Key Features

### 🎨 Modern Dark Theme
- Professional dark color scheme
- Smooth transitions and hover effects
- Responsive design for all screen sizes
- Beautiful typography using Inter font

### 📱 Responsive Design
- Mobile-first approach
- Hamburger menu for mobile navigation
- Flexible grid layouts
- Touch-friendly interface

### 📝 Blog System
- Create new blog posts
- View all posts with excerpts
- Individual post pages
- Automatic date formatting
- Flash messages for user feedback

### 💼 Professional Showcase
- Comprehensive experience timeline
- Featured projects with impact metrics
- Skills and certifications display
- Contact information and social links

### 🚀 Performance
- Optimized CSS with CSS variables
- Minimal JavaScript footprint
- Efficient Flask routing
- SQLite for fast, local database operations

## Customization

### Updating Personal Information
1. Edit the templates to update personal details:
   - `templates/home.html` - Hero section and introduction
   - `templates/about.html` - Personal background and skills
   - `templates/experience.html` - Work experience and achievements
   - `templates/projects.html` - Featured projects and accomplishments
   - `templates/contact.html` - Contact information and social links

### Styling Customization
1. Edit `static/css/style.css` to modify:
   - Color scheme (CSS variables at the top)
   - Typography and spacing
   - Component styles
   - Responsive breakpoints

### Adding New Features
1. Create new routes in `app.py`
2. Add corresponding templates in `templates/`
3. Update navigation in `templates/base.html`
4. Add any required styling to `static/css/style.css`

## Database

The application uses SQLite for the blog functionality:
- **Database file**: `portfolio.db` (auto-created)
- **Tables**: `blog_post` (id, title, content, date_posted)
- **Migrations**: Automatic table creation on first run

## Deployment

### Local Development
```bash
python app.py
```
Access at: `http://localhost:5000`

### Production Deployment
For production deployment, consider:
1. Setting `debug=False` in `app.py`
2. Using a production WSGI server (Gunicorn, uWSGI)
3. Setting a secure `SECRET_KEY`
4. Configuring environment variables
5. Using a production database (PostgreSQL, MySQL)

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance Features

- CSS Grid and Flexbox for efficient layouts
- Optimized images and icons
- Minimal JavaScript for core functionality
- Efficient Flask routing and templating
- SQLite for fast local database operations

## Contributing

This is a personal portfolio website. If you'd like to use this as a template:
1. Fork the repository
2. Update personal information in templates
3. Customize styling to match your preferences
4. Update this README with your information

## License

This project is open source and available under the [MIT License](LICENSE).

## Contact

- **Email**: manish25102@gmail.com
- **LinkedIn**: [linkedin.com/in/manishyadav12](https://linkedin.com/in/manishyadav12)
- **Phone**: +91 7376356606

---

Built with ❤️ using Flask, HTML5, CSS3, and JavaScript