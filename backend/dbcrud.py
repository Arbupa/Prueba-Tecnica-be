from pymongo import MongoClient, database
from bson.objectid import ObjectId


# function to return the database from the connection to mongo.
def connect_to_db():
    host = "localhost"
    port = "4000"
    user = "root"
    password = "example"
    database = "testing"
    client = MongoClient(
        "mongodb://{}:{}@{}:{}".format(user, password, host, port))
    return client[database]


# function to insert data in the database.
def insert(data):
    database = (connect_to_db())
    companiesdata = database.companiesdata
    return companiesdata.insert_one({
        "uuid": data.uuid,
        "name": data.name,
        "description": data.description,
        "symbol": data.symbol,
        "values": data.values,
    }).inserted_id


# function to get all the documents from the collection companiesdata
def get_all():
    database = connect_to_db()
    return database.companiesdata.find()


# function to update the document from the given id.
def update(id, data):
    database = connect_to_db()
    resultado = database.companiesdata.update_one(
        {   # maybe change it for uuid or something else
            '_id': ObjectId(id)
        },
        {
            '$set': {
                "uuid": data.uuid,
                "name": data.name,
                "description": data.description,
                "symbol": data.symbol,
                "values": data.values,
            }
        })
    return "Number of documents modified: " + str(resultado.modified_count)


# function to delete a document from the given ID.
def delete(id):
    database = connect_to_db()
    document = database.companiesdata.delete_one(
        {
            '_id': ObjectId(id)
        }
    )
    return document


# function to get the document from the given ID.
def get_by_id(id):
    database = connect_to_db()
    # try and catch to handle error if the given ID is wrong or not found in database
    try:
        document = database.companiesdata.find_one(
            {
                '_id': ObjectId(id)
            }
        )
        if document:
            return document
    except:
        return ""
