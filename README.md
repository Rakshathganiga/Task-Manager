# Task Management REST API (Django)

A REST API for managing tasks built using **Python, Django, and Django REST Framework**.  
This project uses **in-memory storage only** (no database).

---

## Setup & Run Instructions

### Prerequisites
- Python 3.x
- pip

### Steps
```bash
# Install dependencies
pip install django djangorestframework

# Start Django project
django-admin startproject task_manager
cd task_manager

# Start app
python manage.py startapp tasks

# Run server
python manage.py runserver
```
---

## Task Management REST API - Endpoints & Examples

---

### 1. Create Task
- **Method:** POST  
- **URL:** `/tasks`  
- **Description:** Create a new task with a title, optional description, and status.

**Postman**
- Method: POST  
- URL: `http://127.0.0.1:8000/tasks`  
- Body → raw → JSON
```json
{
  "title": "Learn Django",
  "description": "Build task management API",
  "status": "pending"
}
```

### 2. List All Tasks
- **Method:** GET  
- **URL:** `/tasks`  
- **Description:** Retrieve all tasks. Optional filter by status (pending, in_progress, completed).

**Postman**
- Method: GET  
- URL: `http://127.0.0.1:8000/tasks?status=pending`

### 3. Get Task by ID
- **Method:** GET  
- **URL:** `/tasks`  
- **Description:** Retrieve a single task by its unique ID.

**Postman**
- Method: GET  
- URL: `http://127.0.0.1:8000/tasks/<task_id>`

### 4. Update Task
- **Method:** PUT  
- **URL:** `/tasks`  
- **Description:** Update title, description, or status of a task.

**Postman**
- Method: PUT 
- URL: `http://127.0.0.1:8000/tasks/<task_id>`
```json
{
  "status": "pending"
}
```

### 5. Delete Task
- **Method:** DELETE  
- **URL:** `/tasks`  
- **Description:** Delete a task by its ID.

**Postman**
- Method: DELETE  
- URL: `http://127.0.0.1:8000/tasks/<task_id>`

---

## Task Management REST API - Assumptions & Time Spent

### Assumptions & Design Decisions
- In-memory dictionary is used as storage (no database).  
- UUIDs are used for unique task IDs.  
- UTC timestamps are used for `created_at` and `updated_at`.  
- Data resets when the server restarts.  
- Django REST Framework is used for clean API structure and request handling.  
- Endpoints tested using Postman.  
- Task `title` must be 3–100 characters, `description` optional (max 500 characters).  
- Task `status` must be one of: `pending`, `in_progress`, `completed`.  
- All errors are returned in JSON format, e.g., `{ "error": "Task not found" }`.

---

### Time Spent
Approximately **3 hours** in total:  
- API design and implementation  
- Validation and error handling  
- Testing endpoints with Postman
- Writing documentation

