# _*_ coding:utf-8 _*
from pymongo import MongoClient
from getpass import getpass
import os

cliente = MongoClient()
db = cliente.monix

def registrarse():
    
    os.system("cls")

    user = raw_input("User: ")
    password = getpass("Password: ")
    confirm = getpass("Confirm: ")
    email = raw_input("Email: ")

    if password != confirm:
        raw_input("La contraseña no conicide")
        registrarse()
        return
    
    db.usuarios.insert_one({
    "user": user,
    "password": password,
    "email": email
    })    

    raw_input("Se ha registrado al usuario <%s> con exito " % user)    

def iniciar_sesion():
    
    user = raw_input("User: ")
    password = getpass("Password: ")

    doc = db.usuarios.find_one({
        "user": user,
        "password": password,
    }) 

    if not doc:
        raw_input("Acceso Incorrecto")
        return

    raw_input("Bienvenido: %s (%s)" % (doc["user"], doc["password"]))        
