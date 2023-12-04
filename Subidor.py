import requests
import json

# Credenciales de CouchDB
usuario = 'Admin'
contraseña = 'Tr@nsp0rtar'
url = 'http://localhost:5984/'  # la URL de tu instancia de CouchDB

# Nombre de la base de datos en la que quieres almacenar tu documento
nombre_bd = 'prueba'

# Cargar el documento JSON
with open('prueba.json', 'r') as f:
    data = json.load(f)
# Subir el documento a CouchDB
resp = requests.post(f"{url}{nombre_bd}", json=data, auth=(usuario, contraseña))
if resp.status_code in [200, 201, 202]:
    print("Documento subido con éxito:", resp.json())
else:
    print("Error al subir el documento:", resp.json())
