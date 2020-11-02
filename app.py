import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Book, Techer
from auth import AuthError, requires_auth

BOOKS_PER_PAGE = 10


def paginate_Books(request, selection):
  page = request.args.get('page', 1, type=int)
  start =  (page - 1) * BOOKS_PER_PAGE
  end = start + BOOKS_PER_PAGE

  books = [book.format() for book in selection]
  current_books = books[start:end]

  return current_books


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app, resources={r"*": {"origins":"*"}})

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

  @app.route('/techers', methods=['GET'])
  @requires_auth('get:techer')
  def retrive_techers(payload):
    techers = Techer.query.order_by(Techer.type).all()

    if len(techers) == 0:
        abort(404)

    return jsonify({
      'success': True,
      'techers' : {techer.id : techer.type for techer in techers}
    }), 200

  @app.route('/books', methods=['GET'])
  @requires_auth('get:book')  
  def retrieve_books(payload):
    
    selection = Book.query.order_by(Book.id).all()
    current_books = paginate_books(request, selection)
    techers = Techer.query.order_by(Techer.type).all()
    if len(current_books) == 0:
      abort(404)

    return jsonify({
      'success': True,
      'books': current_books,
      'techers': {techer.id: techer.type for techer in techers}
    }), 200

  @app.route('/techers', methods=['POST'])
  @requires_auth('post:techer')
  def create_techer(payload):
    body = request.get_json()

    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_specialty = body.get('specialty', None)
    new_experience = body.get('experience', None)

    try:
      techer = Techer(name=new_name, age=new_age, specialty=new_specialty, experience=new_experience)
      techer.insert()

      selection = Techer.query.order_by(Techer.id).all()
      current_techers = paginate_techers(request, selection)

      return jsonify({
        'success': True,
        'age': new_age,
        'specialty': new_specialty,
        'experience': new_experience,
        'techer': current_techers
      }), 200
    except:
        abort(400)

  @app.route('/books', methods=['POST'])
  @requires_auth('post:book')
  def create_book(payload):
    body = request.get_json()

    new_title = body.get('title', None)
    new_auther = body.get('auther', None)
    new_specialty = body.get('specialty', None)
    new_number_of_pages = body.get('number_of_pages', None)

    try:
      book = Book(title=new_title, auther=new_auther, specialty=new_specialty, number_of_pages=new_number_of_pages)
      book.insert()

      selection = Book.query.order_by(Book.id).all()
      current_books = paginate_books(request, selection)

      return jsonify({
        'success': True,
        'title': new_title,
        'specialty': new_specialty,
        'number_of_pages': new_number_of_pages,
        'book': current_books
      }), 200
    except:
        abort(400)

  @app.route('/techers/<int:techer_id>', methods=['PATCH'])
  @requires_auth('patch:techer')
  def update_techers(payload, techer_id):
    body = request.get_json()
    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_specialty = body.get('specialty', None)
    new_experience = body.get('experience', None)
    
    techer = Techer.query.filter(Techer.id == techer_id).one_or_none()
    if techer is None:
        abort(400)
    try:
        if name:
          techer.new_name = name
        if age:
          techer.new_age = age
        if specialty:
          techer.new_specialty = specialty
        if experience:
          techer.new_experience = experience
        techer.update()
        return jsonify({
          'success': True,
          'techer': techer
        }), 200
    except:
        abort(400)

  @app.route('/techers/<int:techer_id>', methods=['DELETE'])
  @requires_auth('delete:techer')
  def delete_techer(payload, techer_id):
    try:
      techer = Techer.query.filter(Techer.id == techer_id).one_or_none()

      if techer is None:
        abort(422)

      techer.delete()

      return jsonify({
        'success': True,
        'deleted': techer_id
      })

    except:
      abort(422)

  @app.route('/books/<int:book_id>', methods=['DELETE'])
  @requires_auth('delete:book')
  def delete_book(payload, book_id):
    try:
      book = Book.query.filter(Book.id == book_id).one_or_none()

      if book is None:
        abort(422)

      book.delete()

      return jsonify({
        'success': True,
        'deleted': book_id
      })

    except:
      abort(422)

  @app.route('/techers/search', methods=['POST'])
  def search_techer():
    body = request.get_json()

    search_term = body.get('search_term', None)

    try:
      selection = Techer.query.order_by(Techer_id).filter(Techer.title.ilike('%{}%'.format(search_term)))
      current_techers = paginate_techers(request, selection)
    except:
      return jsonify({
        'success': True,
        'techers': current_techers
      })

  @app.route('/books/search', methods=['POST'])
  def search_book():
    body = request.get_json()

    search_term = body.get('search_term', None)

    try:
      selection = Book.query.order_by(Book_id).filter(Book.title.ilike('%{}%'.format(search_term)))
      current_books = paginate_books(request, selection)
    except:
      return jsonify({
        'success': True,
        'books': current_books
      })


  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
                      "success": False, 
                      "error": 422,
                      "message": "unprocessable"
                      }), 422

  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
                      "success": False, 
                      "error": 404,
                      "message": "resource not found"
                      }), 404

  app.register_error_handler(404, not_found)
  
  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
                      "success": False, 
                      "error": 400,
                      "message": "bad request"
                      }), 400
   
  @app.errorhandler(401)
  def Auth_error(error):
      return jsonify({
                  "success": False, 
                  "error": 401,
                  "message": "resource not found"
                  }), 401


  return app

app = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)
