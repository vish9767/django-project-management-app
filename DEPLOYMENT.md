# 🌐 Deployment Guide - Social Booster Media API

## Quick Deployment Options

### Option 1: Railway (Recommended - Easiest)

1. **Sign up at Railway:** https://railway.app/

2. **Deploy from GitHub:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Django

3. **Add Environment Variables:**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=.railway.app
   ```

4. **Railway will automatically:**
   - Install dependencies
   - Run migrations
   - Start the server

5. **Load Sample Data (Optional):**
   - Go to project settings
   - Open terminal
   - Run: `python manage.py populate_data`

**Live in 5 minutes!** ⚡

---

### Option 2: Render

1. **Sign up at Render:** https://render.com/

2. **Create Web Service:**
   - Click "New +"
   - Select "Web Service"
   - Connect your GitHub repo

3. **Configure Service:**
   - **Name:** social-booster-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn social_booster_app.wsgi:application`

4. **Add Environment Variables:**
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=.onrender.com
   PYTHON_VERSION=3.13.1
   ```

5. **Deploy!**

---

### Option 3: Heroku

1. **Install Heroku CLI:** https://devcenter.heroku.com/articles/heroku-cli

2. **Login and Create App:**
   ```bash
   heroku login
   heroku create your-app-name
   ```

3. **Set Environment Variables:**
   ```bash
   heroku config:set SECRET_KEY=your-secret-key-here
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS=.herokuapp.com
   ```

4. **Deploy:**
   ```bash
   git push heroku main
   ```

5. **Run Migrations:**
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py populate_data
   ```

6. **Open App:**
   ```bash
   heroku open
   ```

---

### Option 4: Vercel (Serverless)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Configure Environment:**
   - Add environment variables in Vercel dashboard
   - SECRET_KEY
   - DEBUG=False

**Note:** Vercel is serverless, better for static sites. Railway/Render recommended for Django.

---

## 📋 Pre-Deployment Checklist

Before deploying to production:

### 1. Security Settings
- [ ] Generate new SECRET_KEY
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Review CORS settings

### 2. Database
- [ ] Set up PostgreSQL (for production)
- [ ] Update DATABASE_URL in environment
- [ ] Run migrations on production
- [ ] Backup strategy in place

### 3. Static Files
- [ ] Run `python manage.py collectstatic`
- [ ] Configure static file serving

### 4. Environment Variables
- [ ] All secrets in environment variables
- [ ] No sensitive data in code
- [ ] .env file in .gitignore

### 5. Testing
- [ ] Test all API endpoints
- [ ] Verify external APIs work
- [ ] Check dashboard statistics
- [ ] Test CRUD operations

---

## 🗄️ PostgreSQL Setup (Production)

### Using Supabase (Free PostgreSQL)

1. **Sign up:** https://supabase.com/

2. **Create Project:**
   - New project
   - Note down database credentials

3. **Update .env:**
   ```env
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=postgres
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_HOST=db.xxx.supabase.co
   DB_PORT=5432
   ```

4. **Install psycopg2:**
   ```bash
   pip install psycopg2-binary
   ```

5. **Run Migrations:**
   ```bash
   python manage.py migrate
   python manage.py populate_data
   ```

---

## 🔧 Environment Variables Reference

### Required for All Deployments:
```env
SECRET_KEY=django-insecure-CHANGE-THIS-IN-PRODUCTION
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,.railway.app,.onrender.com
```

### For PostgreSQL:
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=5432
```

### Optional:
```env
WEATHER_API_KEY=your_api_key_if_needed
```

---

## 🚀 Quick Railway Deployment

**Fastest way to deploy (2 minutes):**

1. Push to GitHub
2. Go to https://railway.app/
3. Click "New Project" → "Deploy from GitHub"
4. Select your repo
5. Add environment variables
6. Done! 🎉

Railway provides:
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Auto-deployments on git push
- ✅ Database support
- ✅ Easy environment variables

---

## 📱 Testing Production Deployment

Once deployed, test these endpoints:

```bash
# Replace YOUR_URL with your deployment URL

# Test API root
curl https://YOUR_URL/api/

# Test projects
curl https://YOUR_URL/api/projects/

# Test dashboard
curl https://YOUR_URL/api/dashboard/

# Test external APIs
curl https://YOUR_URL/api/external/quotes/
curl https://YOUR_URL/api/external/weather/?city=London
```

---

## 🐛 Common Deployment Issues

### Issue: Static files not loading
**Solution:**
```bash
python manage.py collectstatic --noinput
```

### Issue: Database connection failed
**Solution:**
- Verify DATABASE_URL environment variable
- Check database credentials
- Ensure database is accessible

### Issue: SECRET_KEY error
**Solution:**
- Generate new secret key:
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Issue: ALLOWED_HOSTS error
**Solution:**
- Add your domain to ALLOWED_HOSTS in .env:
```env
ALLOWED_HOSTS=yourdomain.com,.railway.app,localhost
```

---

## 📊 Post-Deployment Steps

After successful deployment:

1. **Test All Features:**
   - CRUD operations
   - External APIs
   - Dashboard
   - Admin panel

2. **Create Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

3. **Load Sample Data:**
   ```bash
   python manage.py populate_data
   ```

4. **Monitor Logs:**
   - Check for errors
   - Monitor API performance

5. **Documentation:**
   - Update README with live URL
   - Share API documentation

---

## 🎉 Success!

Your application is now live and accessible to the world!

**Share these URLs:**
- **Live App:** https://your-app-url/
- **API Docs:** https://your-app-url/api/
- **GitHub:** https://github.com/yourusername/repo

---

## 📞 Support Resources

- **Django Docs:** https://docs.djangoproject.com/
- **DRF Docs:** https://www.django-rest-framework.org/
- **Railway Docs:** https://docs.railway.app/
- **Render Docs:** https://render.com/docs

---

**Good luck with your deployment!** 🚀
