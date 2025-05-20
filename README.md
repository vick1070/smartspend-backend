# SmartSpend API 💸

A Django REST API for tracking personal expenses with JWT authentication.

## Features
- JWT login (`/api/token/`)
- Authenticated expenses API (`/api/expenses/`)
- Per-user data filtering

## Setup

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
