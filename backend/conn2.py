import pymongo

client = pymongo.MongoClient("mongodb://localhost:3000")
db = client["mi-db"]

# Name
print("Nombre de la DB: ", db.name)

# Crea colección e inserta un registro
print(db.pet.insert_many([
    {
        "name": "firulais",
        "owner": "jahir",
        "specie": "perro"
    },
    {
        "name": "taco",
        "owner": "jonathan",
        "specie": "perro"
    },
    {
        "name": "garfield",
        "owner": "erick",
        "specie": "gato"
    },
    {
        "name": "charlotte",
        "owner": "juan daniel",
        "specie": "araña"
    },
    {
        "name": "solovino",
        "owner": "jorge",
        "specie": "perro"
    },
]))
