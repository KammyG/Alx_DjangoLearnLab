# Django Blog Project

## Overview
A Django-based blog application with user authentication, including registration, login, logout, and profile management.

## Features
- User authentication system
- Profile management
- CSRF protection and password hashing
- Organized URL patterns

## Installation
1. **Clone the Repository:**
   ```sh
   git clone https://github.com/KammyG/Alx_DjangoLearnLab.git
   cd Alx_DjangoLearnLab/django_blog
   ```
2. **Create and Activate a Virtual Environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate  # Windows
   ```
3. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations:**
   ```sh
   python manage.py migrate
   ```
5. **Run the Development Server:**
   ```sh
   python manage.py runserver
   ```
   Access the app at `http://127.0.0.1:8000/`.

## Usage
- **Register:** Visit `/register/` to create an account.
- **Login:** Go to `/login/` and enter credentials.
- **Logout:** Click logout or visit `/logout/`.
- **Profile Management:** Visit `/profile/` to update user details.

## Security
- CSRF protection enabled
- Passwords securely hashed
- Authentication required for profile access

## Contribution
1. Fork the repository.
2. Create a feature branch.
3. Commit and push changes.
4. Open a pull request.



This Django blog project allows users to create, view, update, and delete blog posts.

## Features
- **User Authentication**: Login, Logout, Register
- **CRUD Operations for Blog Posts**
- **Permissions**: Only authors can edit/delete their posts
- **Styled HTML Templates**

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/KammyG/Alx_DjangoLearnLab.git
