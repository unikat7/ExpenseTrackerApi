 Expense Tracker API
This project is focused on building a RESTful Expense Tracker API using Django REST Framework (DRF) with JWT-based authentication.

Authentication
Implements JWT (JSON Web Tokens) for secure authentication using djangorestframework-simplejwt.

Users must be authenticated to interact with most endpoints.

Tokens are obtained using the built-in JWT views.

Core API Endpoints
Method	Endpoint	Description
GET	/api/expenses/	Fetch a paginated list of expenses (2 per page)
GET	/api/expenses/<id>/	Retrieve a specific expense by ID
POST	/api/expenses/	Create a new expense
PUT	/api/expenses/<id>/	Update an existing expense
DELETE	/api/expenses/<id>/	Delete an expense
POST	/api/auth/register/	Register a new user
POST	/api/auth/login/	Obtain JWT access and refresh tokens

Pagination
Expense list endpoint /api/expenses/ supports pagination.

2 results per page are returned by default.

Use query parameters like ?page=2 to navigate pages.

Features Implemented
User registration (/api/auth/register/)

JWT login (/api/auth/login/)

Authenticated access to expenses

Pagination on expense listing

Automatically links expenses to the logged-in user

Future Plans
Implement permission-based access control so users can only update/delete their own expenses.

Add user-specific filters and search.

