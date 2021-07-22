from pymongo import MongoClient, database
from bson.objectid import ObjectId
# ESTE ES EL QUE FUNCIONA POR NADA DEL MUNDO BORRAR NADA!!!!!!!!!


# function to return the database from the connection to mongo.
def connect_to_db():
    host = "localhost"
    port = "4000"
    user = "root"
    password = "example"
    database = "testing"
    client = MongoClient(
        "mongodb://{}:{}@{}:{}".format(user, password, host, port))
    #print("succesfully conected!")
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
def get_all_data():
    database = connect_to_db()
    return database.companiesdata.find()


# function to update the document from the given id.
def update_data(id, data):
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
    return "Number of documents modified: "+resultado.modified_count


def delete_data(id):
    database = connect_to_db()
    document = database.companiesdata.delete_one(
        {
            '_id': ObjectId(id)
        }
    )


def get_data_by_id(id):
    database = connect_to_db()
    document = database.companiesdata.find_one(
        {
            '_id': ObjectId(id)
        }
    )
    return document

# print(insert())

#product = Product("a", 4, 56)

# product.cantidad = 1
# product.nombre = "Sal"
# product.precio = 39
# print(product)
# print(insert(product))
