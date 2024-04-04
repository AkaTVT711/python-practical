## Overview

This is a pool where I can swim with multiple Python frameworks.

## Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python 3.10+
- PostgreSQL
- pip (Python package installer)

## Getting Started

To get started with the tutorial, follow these steps:

1. Clone the repository to your local machine:
   git clone https://github.com/AkaTVT711/python-practical
   cd python-practical


2. Set up a virtual environment (optional but recommended):
   python -m venv venv


3. Activate the virtual environment:

- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install dependencies:
   ```
    pip install -r requirements.txt
    ```

5. Initialize the database schema:
   ```
    alembic upgrade head
   ```

6. Run the FastAPI application:
   ```
   uvicorn app.main:app --reload
   ```

7. Open your web browser and navigate to `http://localhost:8000/docs` to access the interactive API documentation (
   Swagger UI).

## Project Structure

The project structure is organized as follows:

- `app`: Contains the FastAPI application code.
- `__init__`: The file __init__.py is just an empty file, but it tells Python that sql_app with all its modules (Python files) is a package.
- `crud.py`: Implements CRUD operations for database models.
- `database.py`: Implements CRUD operations for database models.
- `main.py`: Defines the FastAPI application instance and includes routers.
- `models.py`: Defines database models using SQLAlchemy ORM.
- `schemas.py`:  Defines Pydantic models.


```bash
  python-practical/
    ├── alembic/
        ├── versions
    ├── app/
        ├── __init__.py
        ├── crud.py
        ├── database.py
        ├── main.py
        ├── models.py
        └── schemas.py
    └── requirements.txt
    └── alembic.ini
    └── README.md
```
