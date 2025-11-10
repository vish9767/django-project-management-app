# Social Booster Media - Demo Task Submission

## 📝 Submission Overview

This project demonstrates full-stack development capabilities with Django, REST APIs, third-party integrations, and data visualization.

## ✅ Requirements Checklist

### 1. CRUD Functionality via REST APIs ✓
- **Projects API**: Complete CRUD operations
  - Create: `POST /api/projects/`
  - Read: `GET /api/projects/` and `GET /api/projects/{id}/`
  - Update: `PUT/PATCH /api/projects/{id}/`
  - Delete: `DELETE /api/projects/{id}/`
  
- **Tasks API**: Complete CRUD operations
  - Create: `POST /api/tasks/`
  - Read: `GET /api/tasks/` and `GET /api/tasks/{id}/`
  - Update: `PUT/PATCH /api/tasks/{id}/`
  - Delete: `DELETE /api/tasks/{id}/`

### 2. Third-Party API Integration ✓
- **Random Quotes API**: `GET /api/external/quotes/`
  - Integrates with Quotable.io API
  - Fetches inspirational quotes
  
- **Weather API**: `GET /api/external/weather/?city=London`
  - Integrates with wttr.in weather service
  - Fetches real-time weather data for any city

### 3. Data Visualization / Reporting ✓
- **Dashboard Endpoint**: `GET /api/dashboard/`
  - Total projects and budget statistics
  - Project status breakdown
  - Task completion rates and analytics
  - Priority distribution
  - Top clients by project count
  - Recent activity tracking

### 4. Technology Stack ✓
- **Backend**: Django 5.2.8
- **API Framework**: Django REST Framework 3.16.1
- **Database**: SQLite (PostgreSQL-ready configuration)
- **Dependencies**: See `requirements.txt`

## 🚀 Quick Start

1. **Setup Environment**:
   ```bash
   python -m venv venv
   venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

2. **Run Migrations**:
   ```bash
   venv\Scripts\python.exe manage.py migrate
   ```

3. **Load Sample Data**:
   ```bash
   venv\Scripts\python.exe manage.py populate_data
   ```

4. **Start Server**:
   ```bash
   venv\Scripts\python.exe manage.py runserver
   ```

5. **Access Application**:
   - API Root: http://localhost:8000/
   - API Endpoints: http://localhost:8000/api/
   - Admin Panel: http://localhost:8000/admin/

## 🧪 Testing the Application

### Method 1: Using Browser
Visit these URLs directly in your browser:
- http://localhost:8000/api/projects/
- http://localhost:8000/api/tasks/
- http://localhost:8000/api/dashboard/
- http://localhost:8000/api/external/quotes/
- http://localhost:8000/api/external/weather/

### Method 2: Using cURL
```bash
# List all projects
curl http://localhost:8000/api/projects/

# Get dashboard statistics
curl http://localhost:8000/api/dashboard/

# Get external data
curl http://localhost:8000/api/external/quotes/
```

### Method 3: Using Python Script
```bash
venv\Scripts\python.exe test_api.py
```

## 📁 Project Structure

```
proj3_Socail_booster/
├── api/                      # Main application
│   ├── models.py             # Database models (Project, Task)
│   ├── serializers.py        # DRF serializers
│   ├── views.py              # API views and logic
│   ├── urls.py               # API routing
│   └── admin.py              # Admin configuration
├── social_booster_app/       # Project settings
│   ├── settings.py           # Django configuration
│   └── urls.py               # Main URL routing
├── README.md                 # Full documentation
├── SUBMISSION.md             # This file
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables
├── .gitignore               # Git ignore rules
├── Procfile                 # Deployment config
└── test_api.py              # API test script
```

## 💡 Key Features

1. **Clean Code Architecture**
   - Separation of concerns
   - RESTful design principles
   - Comprehensive error handling
   - Well-documented code

2. **Scalable Database Design**
   - Normalized data structure
   - One-to-many relationships
   - Proper indexing and constraints

3. **API Best Practices**
   - Proper HTTP methods
   - Status codes
   - Filtering and pagination
   - Serialization optimization

4. **Production Ready**
   - Environment-based configuration
   - CORS support
   - Static file handling
   - Deployment configurations

## 🎯 Design Decisions

1. **SQLite for Simplicity**: Using SQLite for easy setup and demonstration. Can switch to PostgreSQL/Supabase by updating `.env` file.

2. **Free External APIs**: Chose public APIs that don't require API keys for easy testing and demonstration.

3. **Sample Data Generator**: Created management command to populate realistic test data.

4. **Comprehensive Dashboard**: Built rich analytics endpoint showcasing data aggregation and reporting capabilities.

5. **Human-Readable Code**: Focused on clarity and maintainability with proper naming conventions and documentation.

## 🔄 Database Schema

### Project Model
- id (Primary Key)
- title
- description
- client_name
- budget (Decimal)
- status (Choice: planning, in_progress, completed, on_hold)
- start_date
- end_date (Optional)
- created_at
- updated_at

### Task Model
- id (Primary Key)
- project (Foreign Key to Project)
- name
- description
- priority (Choice: low, medium, high)
- completed (Boolean)
- due_date (Optional)
- created_at

## 🌐 Deployment Instructions

### Option 1: Heroku
```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py populate_data
```

### Option 2: Railway
- Connect GitHub repository
- Add environment variables from `.env`
- Railway will auto-deploy

### Option 3: Render
- Connect GitHub repository
- Set build command: `pip install -r requirements.txt`
- Set start command: `gunicorn social_booster_app.wsgi:application`

## 📊 Sample API Responses

### Dashboard Statistics
```json
{
  "overview": {
    "total_projects": 5,
    "total_budget": 215000.00,
    "average_budget": 43000.00
  },
  "project_status": {
    "planning": 2,
    "in_progress": 2,
    "completed": 1
  },
  "tasks": {
    "total_tasks": 17,
    "completed_tasks": 8,
    "completion_rate": 47.06
  }
}
```

## 🎓 Learning Outcomes Demonstrated

- ✅ Django REST Framework proficiency
- ✅ Database modeling and relationships
- ✅ API design and implementation
- ✅ Third-party API integration
- ✅ Data aggregation and reporting
- ✅ Code documentation
- ✅ Version control (Git)
- ✅ Deployment configuration

## 📞 Contact

Submitted for: Social Booster Media  
Position: Full Stack Developer  
Submission Date: November 9, 2024

---

**Note**: This project was built with attention to code quality, best practices, and real-world application patterns. All requirements have been successfully implemented and tested.
