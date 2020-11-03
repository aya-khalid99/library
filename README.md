# library
- Is a website to help pepole how want to learn a new skills you find a lot of books and with every book you see a teacher how nelp you to learn that book an a seem time you can add any book you want and we  get you a teacher to help you.
- I do this project for people who need to learn new thinks and they have problem with time or they dont need to git out home so they can learn from any where and any time , i get help them to do what they want in any time they want with help and advice from teachers. 
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```
or we can use:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.
##### Key Dependencies
- Flask is a lightweight backend microservices framework. Flask is required to handle requests and responses.
- SQLAlchemy is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.
- Flask-CORS is the extension we'll use to handle cross origin requests from our frontend server.
- Gunicorn is the production ready server which we will be using to deploy our app.
### Authentication
Role Based Access Control (RBAC) has been configured using Auth0. Three user profiles were created and each assigned one of the following rules:
- casting assistant
- casting director
- executive producer
Each role has a unique bearer token, which will be used to authorise the requests available to that particular role. The tokens can be found in the setup.sh file
## Setup Auth0
- Create a new Auth0 Account
- Select a unique tenant domain
- Create a new, single page web application
- Create a new API
- in API Settings:
  - Enable RBAC
  - Enable Add Permissions in the Access Token
- Create new API permissions:
  - get:teacher
  - get:book
  - post:teacher
  - post:book
  - patch:teacher
  - delete:teacher
  - delete:book
- Create new roles for:
  - manger
    - can get:teacher/book
    - can post:teacher/book
    - can patch:teachers
    - can delete:teaher/book
  - clint
    - can get:teacher/book
- Test your endpoints with Postman.
  - Register 3 users - assign the Producer role to one and Director role to the other and Assistant role to the third.
  - Sign into each account and make note of the JWT.
  - Import the postman collection ./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json
  - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs).
  - Run the collection and correct any errors.
  - Export the collection overwriting the one we've included so that we have your proper JWTs during review!
## Database Setup
you have to add a new database manually , use the code here:
```bash
CREATE DATABASE library
```
## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```
## heroku link 
```bash
https://floating-garden-04274.herokuapp.com/
```
## API-endpoint
### TEACHER
#### Get 
- get a list of all teachers an website.
- sample: curl http://127.0.0.1:5000/techers
#### Patch
- to update the data of teacher like experience, specialty or age . 
#### Post
- to add new teacher to the website.
- curl http://127.0.0.1/techers?page=3 -X POST -H "Content-Type: application/json" -d 
#### Delete 
- to delete any teacher we want from website.
- curl -X DELETE http://127.0.0.1:5000/techers/16?page=2
### BOOK
#### Get
- get a list of book we have in website.
- sample: curl http://127.0.0.1:5000/books
#### Post
- to add new book to the website.
- curl http://127.0.0.1/books?page=3 -X POST -H "Content-Type: application/json" -d 
#### Delete 
- to delete a book from website.
- curl -X DELETE http://127.0.0.1:5000/books/16?page=2
### Error
- 400: bad request
- 401: resource not found
- 404: not found
- 422: unprocessable



