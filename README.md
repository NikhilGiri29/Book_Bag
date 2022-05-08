# LibraryMS

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
Table bhi add karlo
```

#### Run the server locally
```bash
$ uvicorn app.main:app --reload
```