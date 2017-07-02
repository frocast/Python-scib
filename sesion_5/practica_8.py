from pymongo import MongoClient

client = MongoClient()

db = client.cic

db.personas.insert_many([
    {
        "nombre": "ana",
        "edad": 33,
        "sexo": "mujer",
        "colores": ["Rojo", "Azul"],
        "numeros": [2, 8 .5]
    },
    {
        "nombre": "ana",
        "edad": 33,
        "sexo": "mujer",
        "colores": ["Rojo", "Azul"],
        "numeros": [2, 8 .5]
    },
    {
        "nombre": "ana",
        "edad": 33,
        "sexo": "mujer",
        "colores": ["Rojo", "Azul"],
        "numeros": [2, 8 .5]
    },
])