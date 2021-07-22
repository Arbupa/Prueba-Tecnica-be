from flask import Flask
from flask.globals import request
from dbcrud
app = Flask(__name__)


# POST http method to create and insert data.
@app.route('/companies', methods=['POST'])
def create_data():
    # get the data from json request
    name = request.json['name']
    # if's to validate the data and return their respective error
    # also the prints to have the errors on console.
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
        err = "Error: must fill all fields"
        print(err)
        return err, 400

    return {'message': 'received'}


if __name__ == "__main__":
    app.run(debug=True, port=5000)
