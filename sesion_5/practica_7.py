# _*_ coding:utf-8 _*_
import monix
import os


def menu():
    os.system("cls")
    print "Bienvenido a HomeCalc V1.0"
    print "-" * 60
    print "Selecciona una Opcion"
    print "\t1.- iniciar Sesion"
    print "\t2.- Registrarse"
    print "\t3.- Sañir"

    opt = int(raw_input("> "))
    
    if opt == 1:
        monix.iniciar_sesion()
    elif opt == 2:
        monix.registrarse()
    elif opt == 3:
        monix.cliente.close()
        return
    else:
        raw_input("Opcion invalida")    
    
    menu()

menu()
