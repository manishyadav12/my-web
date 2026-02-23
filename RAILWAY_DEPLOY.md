# Deploy to Railway

This guide will help you deploy your Flask portfolio to Railway.

## Prerequisites

1. **Git repository**: Your code needs to be in a Git repository
2. **Railway account**: Sign up at [railway.app](https://railway.app)
3. **GitHub/GitLab connection**: Link your Railway account to your Git provider

## Deployment Steps

### 1. Push to Git Repository

```bash
# If not already a git repository
git init
git add .
git commit -m "Initial commit for Railway deployment"

# Push to your Git provider (GitHub, GitLab, etc.)
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

### 2. Create Railway Project

1. Go to [railway.app](https://railway.app)
2. Click "Start a New Project"
3. Select "Deploy from GitHub repo" (or your Git provider)
4. Choose your portfolio repository
5. Railway will automatically detect it's a Python app

### 3. Add PostgreSQL Database (Optional)

If you want to use the blog functionality:

1. In your Railway project dashboard
2. Click "New" → "Database" → "Add PostgreSQL"
3. Railway will automatically set the `DATABASE_URL` environment variable

### 4. Configure Environment Variables

Add these in your Railway project settings:

- `SECRET_KEY`: Generate a secure secret key
- `FLASK_DEBUG`: Set to `False`
- `FLASK_ENV`: Set to `production`

### 5. Deploy

Railway will automatically deploy when you push to your main branch!

## Files Configured for Railway

✅ `railway.toml` - Railway configuration  
✅ `Procfile` - Process definition  
✅ `requirements.txt` - Dependencies  
✅ `runtime.txt` - Python version  
✅ `gunicorn.conf.py` - Production server config  
✅ `app.py` - Updated for Railway compatibility  

## Custom Domain (Optional)

1. In Railway dashboard → Settings → Domains
2. Add your custom domain
3. Update your DNS settings as instructed

## Monitoring

- Railway provides built-in logs and metrics
- Health check endpoint: `/health`
- Auto-restart on failures configured

## Local Development

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
```

## Troubleshooting

- Check Railway logs in the dashboard
- Ensure all environment variables are set
- Verify your Git repository is properly connected
- Database issues: Check PostgreSQL connection in Railway dashboard

Happy deploying! 🚀