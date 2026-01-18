# Bank-of-Spain-Secure-api
A secure FastAPI-based banking backend that handles user registration, prevents duplicate records, and stores passwords using industry-standard hashing.

---

# 🏦 Bank of Spain – Secure Backend API

A secure backend API built with **FastAPI** that simulates a banking-style user registration system.
The project focuses on **password security**, **duplicate data prevention**, and **clean backend logic**, all implemented clearly in a **single file**.

This project is designed for **portfolio presentation** and to demonstrate real-world backend concepts.

---

## ✨ Features

* 🔐 **Secure Password Hashing**
  Passwords are hashed using **Passlib (bcrypt)** before being stored in the database.

* 🚫 **Duplicate Entry Protection**
  Prevents inserting duplicate users by handling database integrity errors and returning meaningful messages.

* ⚡ **FastAPI Framework**
  High-performance backend with automatic API documentation.

* 🗄️ **PostgreSQL Database**
  Uses PostgreSQL with SQLAlchemy ORM for reliable and structured data storage.

* 🧠 **Single-File Implementation**
  Entire application logic (routes, models, database setup, hashing) is written in one well-organized file for clarity.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** FastAPI
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Security:** Passlib (bcrypt)

---

## 📂 Project Structure

```
bank-of-spain-secure-api/
│
├── main.py     

```

---

## 🚀 How the Application Works

1. User sends registration data via API
2. Application checks if the user already exists
3. Password is securely hashed
4. Data is stored in PostgreSQL
5. API returns a success or error response

---

## 📘 API Documentation

FastAPI automatically generates interactive API docs:

* Swagger UI

  ```
  http://localhost:8000/docs
  ```

* ReDoc

  ```
  http://localhost:8000/redoc
  ```

---

## 📌 Sample API Responses

### Duplicate User

```json
{
  "detail": "User already exists"
}
```

### Successful Registration

```json
{
  "message": "User registered successfully"
}
```

---

## 🔒 Security Notes

* Passwords are never stored in plain text
* Hashing is applied before database insertion
* Sensitive data is not exposed in API responses

---

## 🎯 Project Purpose

This project demonstrates:

* Backend API development using FastAPI
* Secure password handling best practices
* Database integrity and error handling
* Writing clean and readable backend code

Suitable for **GitHub portfolio**, **resume**, and **backend interviews**.

---

## 👤 Author

**Aliii**
Engineer | Backend Developer

---

## 📎 Disclaimer

This project is created for learning and portfolio purposes.



