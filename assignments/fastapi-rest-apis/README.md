# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API for a small library using FastAPI. Practice defining HTTP endpoints, validating request data with Pydantic, and returning appropriate status codes and error responses.

## 📝 Tasks

### 🛠️ Create Read Endpoints

#### Description
Use the provided starter code to create an API for managing books. Install dependencies with `python -m pip install fastapi uvicorn`, then start the development server with `uvicorn starter-code:app --reload`. Open `http://127.0.0.1:8000/docs` to try your endpoints.

#### Requirements
Completed program should:

- Define a `Book` model with an integer `id`, a `title`, and an `author`
- Implement `GET /books` to return all books
- Implement `GET /books/{book_id}` to return one book, or a 404 response when its ID does not exist

### 🛠️ Add and Update Books

#### Description
Add endpoints that accept validated book data and update the in-memory collection. Use the starter `BookCreate` model for incoming data.

#### Requirements
Completed program should:

- Implement `POST /books` to create and return a book with a unique ID and a 201 status code
- Implement `PUT /books/{book_id}` to replace a book's title and author
- Return a 404 response when an update targets a book that does not exist
- Return a 422 validation response when required request fields are missing or have the wrong type

### 🛠️ Delete and Test the API

#### Description
Complete the API by adding deletion, then use the interactive documentation to test successful requests and error cases.

#### Requirements
Completed program should:

- Implement `DELETE /books/{book_id}` to remove a book and return a 204 status code
- Return a 404 response when a delete targets a book that does not exist
- Test each endpoint in `/docs`, including at least one invalid ID and one invalid request body
- Keep the book collection in memory; a database is not required