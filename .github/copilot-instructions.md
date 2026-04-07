# SmartSpend Backend - AI Coding Guidelines

## Project Overview
This is a Django REST API for personal expense tracking with JWT authentication. The API allows users to manage their expenses (CRUD operations) while categories are shared globally.

## Architecture
- **Framework**: Django 5.2.1 with Django REST Framework (DRF) and Simple JWT
- **Database**: SQLite (development), configured in `smartspend_backend/settings.py`
- **Apps**: Single `expenses` app containing models, serializers, views, and URLs
- **Authentication**: JWT-based via `rest_framework_simplejwt`
- **Data Flow**: 
  - Users authenticate via `/api/token/` to get JWT tokens
  - Expenses are filtered by authenticated user (`user` field)
  - Categories are global (no user filtering)

## Key Components
- **Models** (`expenses/models.py`): `Expense` (user-specific) and `Category` (global)
- **Serializers** (`expenses/serializers.py`): Standard ModelSerializers with `user` as read-only on Expense
- **Views** (`expenses/views.py`): DRF generics (ListCreate, RetrieveUpdateDestroy) with authentication on expenses
- **URLs** (`expenses/urls.py`): API endpoints under `/api/` (included from `smartspend_backend/urls.py`)

## Developer Workflows
- **Setup**: `python3 -m venv env && source env/bin/activate && pip install -r requirement.txt && python manage.py migrate && python manage.py createsuperuser && python manage.py runserver`
- **Migrations**: `python manage.py makemigrations expenses && python manage.py migrate`
- **Testing**: No tests implemented yet; add to `expenses/tests.py` using DRF's APITestCase
- **Debugging**: Print statements in views (e.g., `print(">>> request.user:", self.request.user)`) for user verification

## Code Patterns & Conventions
- **Models**: Include `__str__` methods for admin readability (e.g., `return f"{self.title} - ${self.amount}"`)
- **Views**: 
  - Override `get_queryset()` to filter by `self.request.user` for user-specific data
  - Use `perform_create()` to set `user=self.request.user` on creation
  - Permission classes: `[permissions.IsAuthenticated]` for protected endpoints
- **Serializers**: Set `read_only_fields = ['user']` to prevent user spoofing
- **URLs**: Name patterns like `expense-list`, `category-detail` (though note: category detail URL currently uses wrong view class)
- **Dependencies**: Listed in `requirement.txt` (singular naming convention)

## Common Patterns
- **User Filtering**: Always filter querysets by user for privacy: `return Expense.objects.filter(user=self.request.user)`
- **Global Data**: Categories are shared; no auth required for read/create
- **JWT Auth**: Use `/api/token/` for login, include `Authorization: Bearer <token>` in requests

## Known Issues
- `expenses/urls.py`: Category detail view (`categories/<int:pk>/`) incorrectly uses `CategoryListCreateView` instead of `CategoryDetailView`

## File Structure
- `smartspend_backend/`: Project settings and main URLs
- `expenses/`: App logic (models, views, serializers, URLs)
- `env/`: Virtual environment (activate with `source env/bin/activate`)
- `db.sqlite3`: Development database</content>
<parameter name="filePath">/home/vick1070/smartspend-project/.github/copilot-instructions.md