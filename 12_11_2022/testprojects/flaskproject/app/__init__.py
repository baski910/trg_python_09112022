import os
from flask_api import FlaskAPI
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    from .models import Book
    app = FlaskAPI(__name__,instance_path=os.getcwd(),instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)


    @app.route('/booklists',methods=['GET','POST'])
    def booklists():
        if request.method == 'POST':
            title = str(request.data.get('title',''))
            if title:
                book = Book(title=title)
                book.save()
                response = jsonify(
                    {
                        'id': book.id,
                        'title': book.title
                    }
                )
                response.status_code = 201
                return response
        else:
            books = Book.get_all()
            results = []
            for book in books:
                d1 = {
                    'id': book.id,
                    'title': book.title
                }
                results.append(d1)
            response = jsonify(results)
            response.status_code = 200
            return response

    return app