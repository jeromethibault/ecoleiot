from flask import (
    Flask,jsonify,request
)
from db.book import (
    findAll, save, delete, update
)

app = Flask(__name__)
       
@app.route('/book', methods=['GET'])
def getBooks():
    results = findAll()
    return jsonify(results)

@app.route('/book', methods=['POST'])
def saveBook():
    # TODO
    return

@app.route('/book', methods=['DELETE'])
def deleteBook():
    # TODO
    return

@app.route('/book', methods=['PUT'])
def updateBook():
    # TODO
    return
    
app.run()