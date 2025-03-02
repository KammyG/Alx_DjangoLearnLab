"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file (Best practice for storing secrets)
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: Keep the secret key secret in production!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "fallback-secret-key") # Load from environment

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = False  # Disable Debug in Production

ALLOWED_HOSTS = ['yourdomain.com', '127.0.0.1', 'localhost']  # Set allowed hosts

# Redirect to home page after login/logout
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
    'bookshelf',
    'csp',  # Content Security Policy Middleware
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'csp.middleware.CSPMiddleware',  # Add CSP Middleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',  # Moved below CommonMiddleware
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static Files
STATIC_URL = '/static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "bookshelf.CustomUser"

# ========== SECURITY ENHANCEMENTS ========== #

# 🔒 Secure HTTP Headers
SECURE_BROWSER_XSS_FILTER = True  # Prevents XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME-type sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevent Clickjacking attacks
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# 🔒 Secure Cookies
SESSION_COOKIE_SECURE = True  # Prevent session hijacking (Only HTTPS)
CSRF_COOKIE_SECURE = True  # Prevent CSRF attacks (Only HTTPS)
CSRF_COOKIE_HTTPONLY = True  # Prevent JavaScript from accessing CSRF cookie
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript from accessing session cookie

# 🔒 CSRF Protection
CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com']

# 🔒 HTTP Strict Transport Security (HSTS) - **Enable only in production**
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 🔒 Content Security Policy (CSP) - Mitigates XSS Attacks
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")  # Remove `'unsafe-inline'` if not needed
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # Remove `'unsafe-inline'` if not needed
CSP_IMG_SRC = ("'self'", "data:")
CSP_FONT_SRC = ("'self'", "https://fonts.googleapis.com", "https://fonts.gstatic.com")

# ========== END SECURITY ENHANCEMENTS ========== #
