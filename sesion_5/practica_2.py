from pymongo import MongoClient

cliente = MongoClient()

db = cliente.cic

docs = db.usuarios.find()

for doc in docs:
    print doc

cliente.close()    
