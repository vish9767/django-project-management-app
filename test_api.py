"""
Simple test script to verify API endpoints
Run this after starting the server with: python manage.py runserver
"""
import requests
import json

BASE_URL = 'http://localhost:8000/api'


def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"📌 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    except:
        print(f"Response: {response.text}")


def test_api():
    """Test all API endpoints"""
    
    print("🚀 Starting API Tests...")
    
    # Test 1: Get all projects
    response = requests.get(f'{BASE_URL}/projects/')
    print_response("GET /api/projects/ - List all projects", response)
    
    # Test 2: Create a new project
    new_project = {
        "title": "API Test Project",
        "description": "This is a test project created via API",
        "client_name": "Test Client",
        "budget": "25000.00",
        "status": "planning",
        "start_date": "2024-01-15"
    }
    response = requests.post(f'{BASE_URL}/projects/', json=new_project)
    print_response("POST /api/projects/ - Create new project", response)
    
    if response.status_code == 201:
        project_id = response.json()['id']
        
        # Test 3: Get single project
        response = requests.get(f'{BASE_URL}/projects/{project_id}/')
        print_response(f"GET /api/projects/{project_id}/ - Get project details", response)
        
        # Test 4: Update project
        update_data = {"status": "in_progress"}
        response = requests.patch(f'{BASE_URL}/projects/{project_id}/', json=update_data)
        print_response(f"PATCH /api/projects/{project_id}/ - Update project", response)
    
    # Test 5: Get all tasks
    response = requests.get(f'{BASE_URL}/tasks/')
    print_response("GET /api/tasks/ - List all tasks", response)
    
    # Test 6: Dashboard statistics
    response = requests.get(f'{BASE_URL}/dashboard/')
    print_response("GET /api/dashboard/ - Dashboard statistics", response)
    
    # Test 7: External API - Quotes
    response = requests.get(f'{BASE_URL}/external/quotes/')
    print_response("GET /api/external/quotes/ - Random quote", response)
    
    # Test 8: External API - Weather
    response = requests.get(f'{BASE_URL}/external/weather/?city=London')
    print_response("GET /api/external/weather/ - Weather data", response)
    
    print("\n" + "="*60)
    print("✅ All API tests completed!")
    print("="*60)


if __name__ == '__main__':
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the server.")
        print("Please make sure the Django server is running:")
        print("  python manage.py runserver")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
