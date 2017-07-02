from pymongo import MongoClient

client = MongoClient()

db = client.cic

db.personas.insert_many([
    {
        "nombre": "ana",
        "edad": 33,
        "sexo": "mujer",
        "colores": ["Rojo", "Azul"],
        "numeros": [8 .5]
    },
    {
        "nombre": "ana",
        "edad": 33,
        "sexo": "mujer",
        "colores": ["Rojo", "Azul"],
        "numeros": [2, 5]
    },
    {
        "nombre": "beto",
        "edad": 53,
        "sexo": "Hombre",
        "colores": ["Verde", "Negro", "Azul"],
        "numeros": [2, 8, 5]
    },
])