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
## roles and permissions
- The JWT includes the RBAC permission claims.
- Access of roles is limited.
- get the Authorization header from the request.
- Decode and verify the JWT using the Auth0 secret.
- i.e. @require_auth(‘get:techer’)
- raise an error if:
  - the token is expired
  - the claims are invalid
  - the token is invalid
  - the JWT doesn’t contain the proper action

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
https://git.heroku.com/floating-garden-04274.git
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



