from pymongo import MongoClient

cliente = MongoClient()

db = cliente.cic
# db.usuarios.delete_many({"nombre": "FRANCISCO"})
RESULT = db.usuarios.update_many(
    {"nombre": "pepe"},
    {"$set": {"VIP": True} }
)

print RESULT.matched_count
print RESULT.modified_count

cliente.close()
