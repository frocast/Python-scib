from pymongo import MongoClient

cliente = MongoClient()

db = cliente.cic

while True:
    nombre = raw_input("Nombre: ")
    correo = raw_input("Corre: ")

    db.usuarios.insert({
    "nombre": nombre,
    "email": correo
})
    
    if  raw_input("Nuevo Usuario?: ") == "no":
        break


cliente.close()