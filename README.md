# LibraryMS

[toc]

## Introduction
Book Bag is a Library Management system built on FastApi. It contains 20 api endpoints to conduct all library activities. This is a complete LMS with all the necessary functionalties.

## Technologies Used

* Python
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* Poetry

## Installation
#### Clone this Repository
```bash
$ mkdir <filename>
$ cd <filename>
$ git init
$ git clone ""
```
#### Create environment and Activate the environment
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```
#### Install All Dependencies
```bash
$ pip install poetry
$ poetry install
```

#### Setup the Database
```bash
$ alembic upgrade head
```

#### Run the server locally
```bash
$ uvicorn app.main:app --reload
```

## API Description

There are 4 Routes i.e. Books, Students, Inventory, Transaction

### Books

#### Get All Books

- Url: http://127.0.0.1:8000/api/books

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  },{...},{...}]
  ```

#### Get Books by Category

- Url: http://127.0.0.1:8000/api/books/category/{category}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  },{...},{...}]
  ```
  
 #### Get Books by Id

- Url: http://127.0.0.1:8000/api/books/{id}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    {
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  }
  ```
  
#### Get Top 5 Favourite Books

- Url: http://127.0.0.1:8000/api/books/favourite

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  },{...},{...}]
  ```
#### Create Book

- Url: http://127.0.0.1:8000/api/books/

- Method: POST

- Input Body:  
	```json
    {
        "name": str,
        "author" : str,
        "category": str,
  }
  ```

- Output: 
  
    ```json
    {
        "book":{"id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
        },
        "stock" : int
  }
  ```
#### Update Book

- Url: http://127.0.0.1:8000/api/books/{id}

- Method: PUT

- Input Body:  
	```json
    {
        "name": str,
        "author" : str,
        "category": str,
  }
  ```

- Output: 
  
    ```json
    {
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  }
  ```
#### Delete Book

- Url: http://127.0.0.1:8000/api/books/{id}

- Method: Delete

- Input Body:  {}

- Output: {} , Response(HTTP_204_NO_CONTENT)

### Students

#### Get All Students

- Url: http://127.0.0.1:8000/api/students

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
        "id": int
        "first_name": str
        "last_name" : str
        "roll_number": str
        "password": str
        "created_at": datetime.datetime
  },{...},{...}]
  ```
  
 #### Get Student by Id

- Url: http://127.0.0.1:8000/api/students/{id}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    {
        "id": int
        "first_name": str
        "last_name" : str
        "roll_number": str
        "password": str
        "created_at": datetime.datetime
  }
  ```
#### Add Student to Database

- Url: http://127.0.0.1:8000/api/students/

- Method: POST

- Input Body:  
	```json
    {
        "first_name": str
        "last_name" : str
        "roll_number": str
  }
  ```

- Output: 
  
    ```json
    {
        "id": int
        "first_name": str
        "last_name" : str
        "roll_number": str
        "password": str
        "created_at": datetime.datetime
  }
  ```
#### Update Student Contact info

- Url: http://127.0.0.1:8000/api/students/{id}

- Method: PUT

- Input Body:  
	```json
    {
        "first_name": str
        "last_name" : str
        "roll_number": str
  }
  ```

- Output: 
  
    ```json
    {
        "id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
  }
  ```
#### Delete Student From Database

- Url: http://127.0.0.1:8000/api/students/{id}

- Method: Delete

- Input Body:  {}

- Output: {} , Response(HTTP_204_NO_CONTENT)

### Inventory

#### Get Entire Inventory

- Url: http://127.0.0.1:8000/api/inventory

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
        "book":{"id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
        },
        "stock" : int
  },{...},{...}]
  ```
  
 #### Get Book Inventory by Id

- Url: http://127.0.0.1:8000/api/inventory/{id}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    {
        "book":{"id": int,
        "name": str,
        "author" : str,
        "category": str,
        "times_issued": int
        },
        "stock" : int
  }
  ```

#### Update Inventory

- Url: http://127.0.0.1:8000/api/inventory/{id}

- Method: PUT

- Input Body:  
	```json
    {
      "book_id": int
    	"stock" : int
  }
  ```

- Output: 
  
    ```json
    {
        "book_id": int
    	"stock" : int
  }
  ```

### Transaction

#### Get All Transactions

- Url: http://127.0.0.1:8000/api/transaction

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
            "student_id": int,
            "issued_at": datetime.datetime,
            "book_id": int
        },{...},{...}]
  ```
  
 #### Get Tranactions by Book Id

- Url: http://127.0.0.1:8000/api/transaction/books/{id}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
   [{
            "student_id": int,
            "issued_at": datetime.datetime,
            "book_id": int
        },{...},{...}]
  ```
 #### Get Tranactions by Student Id

- Url: http://127.0.0.1:8000/api/transaction/students/{id}

- Method: GET

- Input Body:  {}

- Output: 
  
    ```json
    [{
            "student_id": int,
            "issued_at": datetime.datetime,
            "book_id": int
        },{...},{...}]
  ```
  
#### Issue Book

- Url: http://127.0.0.1:8000/api/transaction/

- Method: POST

- Input Body:  
  ```json
  {
	"book_id": int
    "student_id"   : int
  }
	```

- Output: 
  
    ```json
    {
            "student_id": int,
            "issued_at": datetime.datetime,
            "book_id": int
        }
  ```

#### Return book

- Url: http://127.0.0.1:8000/api/transaction/

- Method: Delete

- Input Body:  
  ```json
  {
	"book_id": int
    "student_id"   : int
  }
	```

- Output: {} , Response(HTTP_204_NO_CONTENT)