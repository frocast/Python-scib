# _*_ coding:utf-8 _*_

from pymongo import MongoClient

cliente = MongoClient()

db = cliente["cic"] # cliente.cic

resultado = db.usuarios.insert({
    "_id": "mi_id",
    "nombre": "pepe",
    "email": "pepe@yahoo.com"
})

print resultado

cliente.close()