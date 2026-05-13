# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a simple REST API using FastAPI, including request handling, validation, and in-memory data management.

## 📝 Tasks

### 🛠️	Create Core API Endpoints

#### Description
Build a FastAPI app for managing a small list of books. Implement endpoints to list all books, retrieve one book by ID, and create a new book.

#### Requirements
Completed program should:

- Create a FastAPI application instance
- Implement GET /books to return all books
- Implement GET /books/{book_id} to return a single book or a 404 error when not found
- Implement POST /books to add a new book with required fields id, title, and author


### 🛠️	Add Update and Delete Operations

#### Description
Expand the API to support full CRUD behavior by adding update and delete routes. Ensure responses are clear and appropriate for success and error cases.

#### Requirements
Completed program should:

- Implement PUT /books/{book_id} to update an existing book
- Implement DELETE /books/{book_id} to remove an existing book
- Return proper HTTP status codes for success and missing resources
- Keep data in a simple in-memory list for this assignment
