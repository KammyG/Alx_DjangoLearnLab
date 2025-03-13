# 📚 Advanced API Project - Django REST Framework

## 🔹 Overview
This project implements a Book API using Django REST Framework with Generic Views.

## 📌 API Endpoints
| Endpoint | Method | Description | Authentication |
|----------|--------|------------|----------------|
| `/books/` | `GET` | List all books | ❌ No |
| `/books/<id>/` | `GET` | Retrieve a book | ❌ No |
| `/books/create/` | `POST` | Add a new book | ✅ Yes |
| `/books/<id>/update/` | `PUT` | Update a book | ✅ Yes |
| `/books/<id>/delete/` | `DELETE` | Delete a book | ✅ Yes |

## 🚀 Running the Project
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/Alx_DjangoLearnLab.git
   cd advanced-api-project
