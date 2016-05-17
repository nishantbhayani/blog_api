#!flask/bin/python
import json
import requests
from flask import Flask, abort, make_response, request
from db_handler import DataBaseHandler

# create an application
mysqldb = DataBaseHandler()
app = Flask(__name__)
@app.route('/')
def index():
    return "Blog API"


@app.route('/blog/api/v1.0/view', methods=['GET'])
def view():
    blogs = mysqldb.view()

    if len(blogs) == 0:
        abort(404)

    return json.dumps(blogs, indent=4)


@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps([{'info': 'No blogs found'}]), 404)


@app.route('/blog/api/v1.0/create', methods=['POST'])
def create():
    if not request.json or 'title' not in request.json or 'text' not in request.json \
            or 'publisher_name' not in request.json:
        abort(400)
    mysqldb.create(request.json)
    return (json.dumps({'info': 'blog created successfully'})), 201


@app.route('/blog/api/v1.0/blogs/<int:id>', methods=['PUT'])
def edit(id):
    if not request.json:
        abort(400)

    mysqldb.edit(id, request.json)
    return (json.dumps({'info': 'blog updated successfully'})), 201


@app.route('/blog/api/v1.0/blogs/<int:id>', methods=['DELETE'])
def delete(id):
    mysqldb.delete(id)
    return (json.dumps({'info': 'blog deleted successfully'})), 201

if __name__ == "__main__":
    app.run(debug=True)
