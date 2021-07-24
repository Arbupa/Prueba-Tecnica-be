# Prueba-Tecnica-be

## Instrucciones:

Para ejecutar esta aplicación se necesita tener instalado:

- Docker
- Python3
- pip3

Después de clonar el repositorio, desde la ventana de comandos en el directorio del proyecto ejecutar el comando **_"docker-compose up -d"_** para levantar el contenedor de _Mongo_ y el de _Mongo-express_ (había agregado que ahí mismo se ejecutara la app de Flask, pero al hacerlo todo desde docker-compose me daba error), así que después de haber levantado los contenedores, cambiar de directorio hacia la carpeta **_/backend/_** y allí ejecutar el comando **_"python app.py"_** para ejecutar la api.

## Importante:

Revisar que pip tenga instaladas las librerías que aparecen en el archivo **_"requirements.txt"_** para evitar problemas.

## Enpoints:

- **_GET_** http://localhost:5000/companies
- **_POST_** http://localhost:5000/companies/
- **_PUT_** http://localhost:5000/companies/_mongo id_
- **_DELETE_** http://localhost:5000/companies/_mongo id_
