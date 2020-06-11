# PRUEBA PRÁCTICA - DjangoREST
### Autor: Kevin Rodriguez, Correo: kevinrour19@gmail.com 
### Empresa que realiza la prueba: TurpialDev, pagina Web: https://turpialdev.com/

## Requerimientos
- Python 3.7.7
- Django==3.0.7
- djangorestframework==3.11.0
- django-cors-headers==3.3.0
- psycopg2==2.8.5
- PostgreSQL == 11

De igual forma se tienen todas las depedencias en el entorno virutal (pokemonEnv)

## Instalación
```
	Paso 1) Clonar el repositorio "https://github.com/kevinr18/POKEMON-TEST" rama master.
	paso 2) Activar el entorno Virutal: 
			a) Abra la consola de comandos y ubiquese en la ruta del proyecto
			b) Escriba pokemonEnv\Scripts\Activate
	paso 3) Instalando la Base de Datos:
			a) Descargue e Instale la Base de datos PostgreSQL de la pagina oficial de acuerdo a su S.O https://www.postgresql.org/download/
			b) Una vez instalada cree una base de datos llamada "turpialdb_pokemon"
	paso 4) Migración de tablas a la BD "turpialdb_pokemon":
			a) Abra la consola de comandos e ingrese a la ruta de la primera carpeta con el nombre "pokemon_project" y ejecute el comando "py manage.py makemigrations", luego de esto ejecute el comando "py manage.py migrate"
			b) abra la  BD con cualquier gestor o el por defecto de postgres pgAdmin y verifique que tiene 24 tablas creadas en el Esquema publico de la BD "turpialdb_pokemon".
	paso 5) Correr el servidor Django:
			a) Ejecute el comando "py manage.py runserver"
```
## Login y Tokens
Para obtener un token y poder utilizar los servicios que solicitan autenticación primero debemos registrarnos con un super usuario para esto aplicamos el siguiente comando:
```
	py manage.py createsuperuser
```
En la consola de comandos se solicitará el nombre de usuario, correo y contraseña. Hecho esto se tendra un usuario el cual deberas autenticar para obtener un Token por medio de la siguiente url:
```
	http://localhost:8000/api/v1/login/"
```
El metodo a utilizar sera "POST" con el siguiente Cuerpo:
```
	{
		"username": "escriba aqui su username",
		"password": "escriba aqui su password"
	}
```
Finalmente a la hora de consumir un servicio que requiera autenticación, deberas crear una llave(Key) en la cabecera con el nombre "Authorization" con el valor(value) "Token (colocar aquí su token sin paratensís)"

**NOTA:**
Si deseas registrar mas usario a la aplicación lo podras realizar mediante el panel de Administración que proporciona Django, con el siguiente enlace:
```
	http://localhost:8000/admin/auth/user/
```

## Estructura
En una API RESTful, los endpoints(URL) definen la estructura de la API y cómo los usuarios finales acceden a los datos desde nuestra aplicación utilizando los métodos HTTP: GET, POST, PUT, DELETE.

En este cuadro se indican los endpoint de nuestra aplicación para poder acceder a los diferentes metodos, todas las urls del cuadro se deben utilizar con la siguiente ruta "http://localhost:8000/api/v1/"

Endpoint |HTTP Method | CRUD Method | Nombre del Servicio| Cuerpo | Resultado
-- | -- |-- |-- | -- | --
`login/` | POST | CREATE |Login | N/A | Ingresar con un usuario creado y obtener el Token de acceso
`pokemons/:id/` | GET | READ | Pokemon specie detail | N/A | Obtener los detalles de un pokemon en especifico. 
`pokemons/own/` | GET | READ | Pokemon catch | N/A | Obtener los pokemons en tu party (debe estar autenticado)
`pokemons/own/` | POST | CREATE | Pokemon catch | (A) | Guardar un pokemon en tu "Storage" (debe estar autenticado)
`pokemons/own/:id/` | PUT | UPDATE |Pokemon rename | (B) | Cambia el "nickname" a tu pokemon (debe estar autenticado)
`pokemons/own/:id/` | DELETE | DELETE | Pokemon release | N/A | Eliminar un pokemon de tu "Storage"
`pokemons/own/party/'` | GET | READ | Pokemon party | N/A | Obtener los pokemons en tu "Party"
`regions/` | GET | READ | Regions list | N/A | Obtener todas las Regiones
`regions/:id/` | GET | READ | Regions detail | N/A | Obtener una Region en especifica con sus detalles de ubicación
`location/:id/` | GET | READ | Location detail | N/A | Obtener una Ubicacion en especifica con sus detalles de area
`areas/:id` | GET | READ | Area detail | N/A | Obtener una Area y los detalles de las especies Pokemon pertenecientes a dicha Area

```
	Cuerpo "(A)": 
	{
	"id_pokemons": 93,
	"nick_name": "Pedro",
	"is_party_member": true
	}
```
```
	Cuerpo "(B)"
	{
	"nick_name": "Timmy"
	}
```

