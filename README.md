# Python FastAPI Clean Architecture

A minimal FastAPI project following clean architecture principles.

## Overview

This repository demonstrates a layered FastAPI application with separate modules for authentication, users, todos, and database infrastructure.

## Getting Started

1. Install dependencies:

```bash
pip install -r requirements-dev.txt
```

2. Run the application:

```bash
uvicorn src.main:app --reload
```

## Project Structure

- `src/` - application source code
- `src/api.py` - route registration
- `src/main.py` - FastAPI app instance
- `src/database/` - database configuration and session management
- `src/auth/` - authentication controller, service, models
- `src/users/` - user controller, service, models
- `src/todos/` - todo controller, service, models

## Notes

- The database uses SQLite by default.
- Uncomment `Base.metadata.create_all(bind=engine)` in `src/main.py` to create tables when needed.
- Update `requirements-dev.txt` if additional dependencies are required.
