# Recipe API

This is a simple Django-based API for managing recipes. The API allows to create, update, delete, and list recipes.

## Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (optional but recommended)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/recipe_project.git
   cd recipe_project
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

    ```bash
    python3 manage.py migrate
    ```

### Running the Application

1. Start the development server:

    ```bash
    python3 manage.py runserver
    ```

2. Access the API:

- Visit the home page: `http://127.0.0.1:8000/`
- Access the API documentation (Swagger): `http://127.0.0.1:8000/swagger/`
- Access the API documentation (Redoc): `http://127.0.0.1:8000/redoc/`

#### API Endpoints

- List and Create Recipes: `GET /api/recipes/ and POST /api/recipes/`
- Update a Recipe: `PUT /api/recipes/<int:pk>/`
- Delete a Recipe: `DELETE /api/recipes/<int:pk>/delete/`
