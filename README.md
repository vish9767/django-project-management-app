#  Project Management Application

A full-stack web application built with Django and Django REST Framework, featuring an **interactive frontend** for CRUD operations, third-party API integration, and data visualization capabilities.

**GitHub Repository:** [https://github.com/vish9767/django-project-management-app](https://github.com/vish9767/django-project-management-app)

**Author:** Vishal (vish9767)

## Features

- **Interactive Web Interface**: Complete CRUD operations through a beautiful, responsive frontend
- **Projects Management**: Create, read, update, and delete projects with modal forms
- **Tasks Management**: Manage tasks with priority levels and completion tracking
- **Real-time Dashboard**: Visual statistics and analytics with auto-refresh
- **Third-Party API Integration**: 
  - Random quotes API integration
  - Real-time weather data integration
- **RESTful APIs**: Full REST API support for external integrations
- **PostgreSQL/SQLite Support**: Flexible database configuration (currently using SQLite for simplicity)
- **Admin Interface**: Django admin panel for easy data management
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Well-Structured Code**: Clean, maintainable, and well-documented code

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/vish9767/django-project-management-app.git
cd django-project-management-app
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
venv\Scripts\python.exe  # Use this to run Python commands
```

### 3. Install Dependencies

```bash
venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 4. Environment Configuration

The project includes a `.env` file for configuration. You can modify it if needed:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.sqlite3
DB_NAME=db.sqlite3
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Populate Sample Data (Optional)

```bash
venv\Scripts\python.exe manage.py populate_data
```

This creates 5 sample projects and 17 tasks for testing.

### 7. Create Superuser (Optional)

To access the Django admin panel:

```bash
venv\Scripts\python.exe manage.py createsuperuser
```

### 8. Run the Development Server

```bash
venv\Scripts\python.exe manage.py runserver
```

The application will be available at `http://localhost:8000/`

## Using the Web Interface

### Quick Start
1. Open your browser and navigate to: **http://localhost:8000/**
2. You'll see the interactive project management interface
3. Use the tabs to navigate between sections:
   - **Projects** - Create, edit, delete, and view all projects
   - **Tasks** - Manage tasks for your projects
   - **Dashboard** - View analytics and statistics
   - **External APIs** - Test third-party API integrations

### Projects Management
- Click "**+ Create New Project**" to add a new project
- Fill in the form with project details
- Click "**Edit**" on any project card to update it
- Click "**Delete**" to remove a project (with confirmation)
- Projects are displayed in a beautiful card grid layout

### Tasks Management
- Click "**+ Create New Task**" to add a new task
- Select the project, set priority, and due date
- Mark tasks as completed using the checkbox
- Edit or delete tasks with the action buttons
- Visual priority indicators (color-coded borders)

### Dashboard
- View real-time statistics from your database
- See project status breakdown
- Monitor task completion rates
- Track top clients by project count

### External APIs
- Get random inspirational quotes
- Fetch real-time weather for any city
- All integrated seamlessly into the UI

## API Documentation

### Base URL
```
http://localhost:8000/api/
```

### Available Endpoints

#### 1. Projects API (CRUD Operations)

**List all projects**
```http
GET /api/projects/
```
Query parameters:
- `status`: Filter by status (planning, in_progress, completed, on_hold)
- `client`: Filter by client name (case-insensitive search)

**Create a new project**
```http
POST /api/projects/
Content-Type: application/json

{
  "title": "New Project",
  "description": "Project description",
  "client_name": "Client Name",
  "budget": "50000.00",
  "status": "planning",
  "start_date": "2024-01-01"
}
```

**Get project details**
```http
GET /api/projects/{id}/
```

**Update a project**
```http
PUT /api/projects/{id}/
PATCH /api/projects/{id}/
Content-Type: application/json

{
  "status": "in_progress",
  "budget": "55000.00"
}
```

**Delete a project**
```http
DELETE /api/projects/{id}/
```

#### 2. Tasks API (CRUD Operations)

**List all tasks**
```http
GET /api/tasks/
```
Query parameters:
- `project`: Filter by project ID
- `completed`: Filter by completion status (true/false)

**Create a new task**
```http
POST /api/tasks/
Content-Type: application/json

{
  "project": 1,
  "name": "Task Name",
  "description": "Task description",
  "priority": "high",
  "completed": false,
  "due_date": "2024-02-01"
}
```

**Get task details**
```http
GET /api/tasks/{id}/
```

**Update a task**
```http
PUT /api/tasks/{id}/
PATCH /api/tasks/{id}/
Content-Type: application/json

{
  "completed": true
}
```

**Delete a task**
```http
DELETE /api/tasks/{id}/
```

#### 3. Data Visualization / Dashboard

**Get dashboard statistics**
```http
GET /api/dashboard/
```

Returns comprehensive statistics including:
- Total projects and budget
- Project status breakdown
- Task completion rates
- Priority distribution
- Top clients by project count

#### 4. Third-Party API Integration

**Get random inspirational quote**
```http
GET /api/external/quotes/
```

**Get weather data**
```http
GET /api/external/weather/?city=London
```
Query parameters:
- `city`: City name (default: London)

## Testing the API

### Using cURL

**Get all projects:**
```bash
curl http://localhost:8000/api/projects/
```

**Create a new project:**
```bash
curl -X POST http://localhost:8000/api/projects/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Test Project",
    "description": "A test project",
    "client_name": "Test Client",
    "budget": "10000.00",
    "status": "planning",
    "start_date": "2024-01-01"
  }'
```

**Get dashboard stats:**
```bash
curl http://localhost:8000/api/dashboard/
```

**Get random quote:**
```bash
curl http://localhost:8000/api/external/quotes/
```

### Using Python requests

```python
import requests

# Get all projects
response = requests.get('http://localhost:8000/api/projects/')
print(response.json())

# Create a new project
data = {
    "title": "New Project",
    "description": "Project description",
    "client_name": "Client Name",
    "budget": "50000.00",
    "status": "planning",
    "start_date": "2024-01-01"
}
response = requests.post('http://localhost:8000/api/projects/', json=data)
print(response.json())

# Get dashboard statistics
response = requests.get('http://localhost:8000/api/dashboard/')
print(response.json())
```

## Project Structure

```
proj3_Socail_booster/
├── api/                          # Main application
│   ├── management/
│   │   └── commands/
│   │       └── populate_data.py  # Sample data generator
│   ├── migrations/               # Database migrations
│   ├── admin.py                  # Admin configuration
│   ├── models.py                 # Data models
│   ├── serializers.py            # DRF serializers
│   ├── views.py                  # API views
│   └── urls.py                   # API URL routing
├── social_booster_app/           # Project configuration
│   ├── settings.py               # Django settings
│   ├── urls.py                   # Main URL configuration
│   └── wsgi.py                   # WSGI configuration
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── manage.py                     # Django management script
└── requirements.txt              # Python dependencies
```

## Technology Stack

- **Backend Framework**: Django 5.2.8
- **API Framework**: Django REST Framework 3.16.1
- **Database**: SQLite (easily configurable to PostgreSQL/Supabase)
- **Environment Management**: python-decouple
- **HTTP Requests**: requests library
- **CORS**: django-cors-headers
- **Static Files**: whitenoise
- **Production Server**: gunicorn

## Deployment

### Deployment to Vercel/Railway/Render

1. **Update ALLOWED_HOSTS** in `.env`:
```env
ALLOWED_HOSTS=yourdomain.com,.vercel.app
```

2. **For PostgreSQL/Supabase**, update `.env`:
```env
DB_ENGINE=django.db.backends.postgresql
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_supabase_host
DB_PORT=5432
```

3. **Collect static files**:
```bash
python manage.py collectstatic --noinput
```

4. **Create Procfile** (for platforms like Heroku):
```
web: gunicorn social_booster_app.wsgi --log-file -
```

## Security Notes

- The current `.env` file contains a demo SECRET_KEY for development
- For production, generate a new SECRET_KEY and keep it secure
- Set `DEBUG=False` in production
- Configure proper ALLOWED_HOSTS
- Use environment variables for sensitive data

## Design Decisions

1. **SQLite for Development**: Used SQLite for simplicity and portability. Can be easily switched to PostgreSQL/Supabase by updating environment variables.

2. **DRF ViewSets**: Used ViewSets for automatic CRUD endpoint generation, reducing boilerplate code.

3. **Separate Serializers**: Created different serializers for list and detail views to optimize response payload.

4. **External APIs**: Chose free public APIs (Quotable for quotes, wttr.in for weather) that don't require API keys for easy demonstration.

5. **Data Visualization**: Implemented comprehensive dashboard endpoint that aggregates and presents meaningful statistics.

6. **Sample Data**: Included management command to populate realistic sample data for immediate testing.

## Meeting Requirements

**CRUD Operations**: Full implementation via REST APIs for Projects and Tasks  
**Third-Party API Integration**: Two examples (quotes and weather APIs)  
 **Data Visualization**: Dashboard endpoint with statistics and analytics  
**Django + PostgreSQL**: Django framework with PostgreSQL support (using SQLite for simplicity)  
**Clean Code**: Well-structured, documented, and maintainable code  
**README**: Comprehensive documentation with setup and testing instructions  

## Developer

Created as a demo task for Social Booster Media

## Support

For questions or issues, please refer to the documentation or contact the development team.

---

**Note**: This is a demonstration project showcasing full-stack development capabilities with Django and REST APIs.
