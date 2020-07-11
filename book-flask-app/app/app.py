from flask import (
    Flask,jsonify,request
)
from db.book import (
    findAll, save, delete, update
)
from flask_restplus import Api, Resource, reqparse, fields

app = Flask(__name__)

api = Api(app, version='1.0', title='Books API',
    description='A simple Books API',
)
ns_books = api.namespace('books', description='Books operations')

books_id_arguments = reqparse.RequestParser()
books_id_arguments.add_argument('id', type=int, required=True)

book_definition = api.model('Book Informations', {
    'name': fields.String(required=True),
    'author': fields.String(required=True)
})

@ns_books.route("/")
class books(Resource):

    def get(self):
        results = findAll()
        return jsonify(results)
    
    @api.expect(book_definition)
    def post(self):
        data = request.get_json()
        print(data.get('name'))
        print(data.get('author'))
        save(data.get('name'), data.get('author'))
        resp = jsonify(success=True)
        return resp
    
    @api.expect(books_id_arguments)
    def delete(self):
        data = books_id_arguments.parse_args(request)
        delete(data.get('id'))
        resp = jsonify(success=True)
        return resp

    def put(self):
        # TODO
        return    
    
app.run()