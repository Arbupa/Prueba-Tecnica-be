# Prueba-Tecnica-be

## Instrucciones:

Para ejecutar esta aplicación se necesita tener instalado:

- Docker
- Python3
- pip3

Después de clonar el repositorio, desde la ventana de comandos en el directorio del proyecto ejecutar el comando **_"docker-compose up -d"_** para levantar el contenedor de _mongo_ y el de _mongo-express_ (había agregado que ahí mismo se ejecutara la app de Flask, pero al hacerlo todo desde docker-compose me daba error), así que después de haber levantado los contenedores, cambiar de directorio hacia la carpeta **_/backend/_** y allí ejecutar el comando **_"python app.py"_** para ejecutar la api.

## Importante:

Revisar que pip tenga instaladas las librerías que aparecen en el archivo **_"requirements.txt"_** para evitar problemas.

## Enpoints:

- **_GET_** http://localhost:5000/companies
- **_POST_** http://localhost:5000/companies/
- **_PUT_** http://localhost:5000/companies/_mongo id_
- **_DELETE_** http://localhost:5000/companies/_mongo id_

## Testing

Para ejecutar los archivos de _test_ se necesita tener coriendo con docker el contenedor de _mongo_ para ejecutarlos basta con estar dentro de la ruta **_".../backend/"_** y utilizar el comando **_pytest dbcrud_test.py_** o **_pytest dataclass_test.py_**.

P. D.: En **_localhost/8081_** se puede acceder a _mongo-express_ utilizando el **_user: flink_** con **_pass: quesadilla13_** para manejar las bases de datos de mongo de manera gráfica.
