from flask import Flask
from flask.globals import request
from flask.wrappers import Response
from dbcrud import *
from dataclass import Data
from bson.json_util import dumps


app = Flask(__name__)


# GET http method to get ALL data.
@app.route('/companies', methods=['GET'])
def get_all_data():
    all_documents = get_all()
    # convert cursor mongo object to list
    documents_list = list(all_documents)
    # convert list to json
    json_documents = dumps(documents_list)

    return json_documents, 200


# POST http method to create and insert data.
@app.route('/companies', methods=['POST'])
def create_data():
    # get the data from json request
    name = request.json['name']
   # if's to validate the data and return their respective error
    # also, if an error occurs is printed on console.
    if len(name) > 50:
        err = "Error: the name must be less than 50 characters"
        print(err)
        return err, 400

    description = request.json['description']
    if description and len(description) > 100:
        err = "Error: description must be less than 100 characters"
        print(err)
        return err, 400

    symbol = request.json['symbol']
    if symbol and len(symbol) > 10:
        err = "Error: symbols must be less than 10 characters"
        print(err)
        return err, 400

    # the user cannot send an empty value.
    # all the errors returns a response code 400: BAD REQUEST
    if name == '' or description == '' or symbol == '':
        return fill_all_fields()

    # if there are no errors, we create the object
    new_data = Data(name, description, symbol)

    # then insert into database and print the id object
    print(str(insert(new_data)) + "  inserted succesfully")

    return 'The data was succesfully added', 200


# PUT http method to update with the new data.
@app.route('/companies/<id>', methods=['PUT'])
def update_data(id):
    # get the data from json request
    name = request.json['name']
    # if's to validate the data and return their respective error
    # also, if an error occurs is printed on console.
    if len(name) > 50:
        err = "Error: the name must be less than 50 characters"
        print(err)
        return err, 400

    # get the data from json request
    description = request.json['description']
    if description and len(description) > 100:
        err = "Error: description must be less than 100 characters"
        print(err)
        return err, 400

    # get the data from json request
    symbol = request.json['symbol']
    if symbol and len(symbol) > 10:
        err = "Error: symbols must be less than 10 characters"
        print(err)
        return err, 400

    # first checks if exist data with the ID given, if not, then returns not found
    # if ID exists then get the old data to have the old values in case the user sends an empty field.
    if get_by_id(id):
        old_data = get_by_id(id)
        old_name = old_data['name']
        old_description = old_data['description']
        old_symbol = old_data['symbol']

        # leave old data in case that no all fields wants to change
        if name == "":
            name = old_name
        if description == "":
            description = old_description
        if symbol == "":
            symbol = old_symbol

        # if there are no errors, we create the object
        new_data = Data(name, description, symbol)

        # then insert the new data into database and print the id object
        print(str(update(id, new_data)) + " document updated")

        return 'The data was succesfully updated', 200
    else:
        return not_found()


# DELETE http method to delete document with the given id.
@app.route('/companies/<id>', methods=['DELETE'])
def delete_data(id):
    # first checks if the given id exists, if not return a message error.
    if get_by_id(id):
        print(delete(id))
        return "Erased succesfully", 200
    return not_found()


# Error to handle if not all the fields were filled
@app.errorhandler(400)
def fill_all_fields(error=None):
    message = {
        'url': 'Error from: ' + request.url,
        'message': 'Must fill all the fields.',
        'status': 400
    }

    print(message)
    return message, 400


# Error to handle if the user tries to do a bad request.
# For example, if he tries to delete or update an id not found.
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'url': 'Error from: ' + request.url,
        'message': 'Error: Resource Not Found.',
        'status': 404
    }

    print(message)
    return message, 400


if __name__ == "__main__":
    app.run(debug=True, port=5000)
