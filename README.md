## Overview

This is a pool where I can swim with multiple Python frameworks.

## Prerequisites

Before begin, ensure we have the following prerequisites installed:

- Python 3.10+
- PostgreSQL
- pip (Python package installer)

## Getting Started

![](C:\Users\Admin\Desktop\2024-04-05_000025.png)

To get started with the tutorial, follow these steps:

1. Clone the repository to your local machine:
   git clone https://github.com/AkaTVT711/python-practical
   cd python-practical


2. Creates a virtual environment named 'env'
   virtualenv env


3. Set up a virtual environment

- via WSL:
  ```
  source env/bin/activate
  ```

4. Install dependencies:
   ```
    pip3 install psycopg2-binary
    pip3 install psycopg2
    pip3 install -r requirements.txt
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
