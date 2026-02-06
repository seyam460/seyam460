# Ride Sharing Platform (Django + React + MySQL)

This repository now includes a full-stack ride sharing starter with a Django REST backend and a React frontend.

## Backend (Django)

**Location:** `backend/`

### Setup

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### MySQL Configuration

Set the following environment variables to use MySQL:

```bash
export MYSQL_DATABASE=rideshare
export MYSQL_USER=root
export MYSQL_PASSWORD=yourpassword
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
```

If `MYSQL_DATABASE` is not set, the backend falls back to SQLite for local development.

### Run Migrations & Server

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Frontend (React + Vite)

**Location:** `frontend/`

### Setup

```bash
cd frontend
npm install
```

### Run Dev Server

```bash
npm run dev
```

The frontend expects the backend at `http://localhost:8000/api`. Override with:

```bash
export VITE_API_BASE=http://localhost:8000/api
```

## API Highlights

- `POST /api/auth/register/` - Register rider/driver
- `POST /api/auth/login/` - Login and get token
- `POST /api/rides/request/` - Request a ride
- `POST /api/rides/{id}/assign/` - Assign driver to ride
- `POST /api/rides/{id}/track/` - Push tracking point
- `POST /api/rides/{id}/payment/` - Mock payment capture

Authentication uses token auth with `Authorization: Token <token>` header.
