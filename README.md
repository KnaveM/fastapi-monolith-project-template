# FastAPI Project Template

This is an example FastAPI project with a project structure, a CLI, and an integrated FastAPI Debug Toolbar.

## Requirements

- Python 3.7 or higher
- FastAPI
- Uvicorn
- Click
- SQLAlchemy
- Pydantic
- IPython
- Pytest
- Httpx
- FastAPI Debug Toolbar

## Installation

1. Clone the repository:

2. Create a virtual environment and activate it:

3. Install the dependencies:


## Running the application

Use the `manager.py` script to run various commands:

- Start the server:
```
python manager.py runserver
```

- Start the server with profiling:
```
python manager.py profile
```
- Run the tests:
```
python manager.py test
```
- Start the interactive shell:
```
python manager.py shell
```
- Initialize the database:
```
python manager.py initdb
```


## API documentation

FastAPI automatically generates API documentation using Swagger UI. To access the documentation, start the server and visit `http://127.0.0.1:8000/docs` in your web browser.
