from pymongo import MongoClient

cliente = MongoClient()

db = cliente.cic
# db.usuarios.delete_many({"nombre": "FRANCISCO"})
RESULT = db.usuarios.delete_many({})
print RESULT.deleted_count

cliente.close()
