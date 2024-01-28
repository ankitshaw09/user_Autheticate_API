Certainly! It looks like you've provided a step-by-step guide for setting up a Django project with user authentication using Django Rest Framework (DRF) and Simple JWT. Below is a formatted version that you can use in a README.md file:

---

# User Authentication API

## Step 1: Create Virtual Environment

```bash
# Create a virtual environment
python -m venv venv
```

## Step 2: Create Project and App

```bash
# Create Django project
django-admin startproject user_authenticate_API

# Create Django app
cd user_authenticate_API
python manage.py startapp user
```

### Connect App with Project in `settings.py`

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'user',
]
```

### Install Django Rest Framework and Simple JWT

```bash
pip install djangorestframework
pip install djangorestframework-simplejwt
```

```python
# settings.py

INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    ...
]

# Add JWT Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

# Configure JWT Settings
from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}
```

### Install Django CORS Headers

```bash
pip install django-cors-headers
```

```python
# settings.py

INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://sub.example.com",
    "http://localhost:8080",
    "http://127.0.0.1:9000",
]
```

## Database Setup

```bash
# Create and apply migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

## URLs Configuration

Create `urls.py` in both the project and app directories.

## Views Configuration

Create a class `UserRegistrations` in `views.py`.

## Postman Testing

### 1. Register User

**Endpoint:** `http://127.0.0.1:8000/api/user/register/`

**Request Body:**

```json
{
    "email": "",
    "name": "",
    "password": "",
    "password2": "",
    "tc": true
}
```

**Response:**

```json
{
    "token": {
        "refresh": "...",
        "access": "..."
    },
    "msg": "Registration Successful"
}
```

### 2. Login User

**Endpoint:** `http://127.0.0.1:8000/api/user/login/`

**Request Body:**

```json
{
    "email": "",
    "password": ""
}
```

**Response:**

```json
{
    "token": {
        "refresh": "...",
        "access": "..."
    },
    "msg": "Login Success"
}
```

### 3. Profile User

**Endpoint:** `http://127.0.0.1:8000/api/user/profile/`

**Headers:**

- Key: `Accept`, Value: `application/json`
- Key: `Authorization`, Value: `Bearer <access-token>`

### 4. Change Password User

**Endpoint:** `http://127.0.0.1:8000/api/user/changepassword/`

**Request Body:**

```json
{
    "old_password": "",
    "new_password": "",
    "confirm_password": ""
}
```

### 5. Send Reset Password Email User

**Endpoint:** `http://127.0.0.1:8000/api/user/send-reset-password-email/`

**Request Body:**

```json
{
    "email": ""
}
```

### 6. Reset Password User

**Endpoint:** `http://127.0.0.1:8000/api/user/reset-password/<uid>/<token>`

**Request Body:**

```json
{
    "new_password": "",
    "confirm_password": ""
}
```

---

Feel free to customize and add more details as needed for your project.