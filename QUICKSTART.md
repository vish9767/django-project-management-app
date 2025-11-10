# 🚀 Quick Start Guide - Social Booster Media API

## Complete Setup in 5 Minutes

### Step 1: Environment Setup
```bash
# Navigate to project directory
cd c:\Users\User\Desktop\vishal_test_pro\proj3_Socail_booster

# Virtual environment is already created
# Install dependencies (if not already installed)
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Step 2: Database Setup
```bash
# Migrations are already applied, but if needed:
venv\Scripts\python.exe manage.py migrate

# Load sample data
venv\Scripts\python.exe manage.py populate_data
```

### Step 3: Start the Server
```bash
venv\Scripts\python.exe manage.py runserver
```

### Step 4: Test the Application

**Open in Browser:**
- Home Page: http://localhost:8000/
- API Root: http://localhost:8000/api/
- Dashboard: http://localhost:8000/api/dashboard/
- Projects: http://localhost:8000/api/projects/

**Or run the test script:**
```bash
venv\Scripts\python.exe test_api.py
```

## 🎯 What's Already Done

✅ Virtual environment created  
✅ All dependencies installed  
✅ Django project configured  
✅ Database migrated  
✅ Sample data loaded  
✅ All APIs working  
✅ Documentation complete  

## 📋 Test the Features

### 1. CRUD Operations
Visit: http://localhost:8000/api/projects/
- View all projects (GET)
- Click "POST" to create new project
- Click on a project to view/edit/delete

### 2. Dashboard Analytics
Visit: http://localhost:8000/api/dashboard/
- See project statistics
- Task completion rates
- Budget analysis

### 3. External API Integration
- Quotes: http://localhost:8000/api/external/quotes/
- Weather: http://localhost:8000/api/external/weather/?city=London

## 🔧 Admin Access (Optional)

Create superuser:
```bash
venv\Scripts\python.exe manage.py createsuperuser
```

Then visit: http://localhost:8000/admin/

## 📤 Deployment Checklist

Before deploying:
1. ✅ Update SECRET_KEY in `.env`
2. ✅ Set DEBUG=False
3. ✅ Configure ALLOWED_HOSTS
4. ✅ Set up PostgreSQL (if needed)
5. ✅ Run collectstatic
6. ✅ Push to GitHub
7. ✅ Deploy to chosen platform

## 🐛 Troubleshooting

**Issue: Port already in use**
```bash
# Use a different port
venv\Scripts\python.exe manage.py runserver 8001
```

**Issue: Module not found**
```bash
# Reinstall dependencies
venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Issue: Database errors**
```bash
# Reset database
del db.sqlite3
venv\Scripts\python.exe manage.py migrate
venv\Scripts\python.exe manage.py populate_data
```

## 📞 Support

For detailed documentation, see:
- README.md - Full documentation
- SUBMISSION.md - Submission details
- test_api.py - API testing examples

---

**Everything is ready to go! Just start the server and test the APIs.** 🎉
