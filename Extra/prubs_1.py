# -*- coding:utf-8 -*-
import socket

mi_socket=socket.socket()
mi_socket.connect(("www.sepi.esimez.ipn.mx", 80))
contador = 0

while True:
    mensaje="E"*512
    if mi_socket.send(mensaje): 
        #print "Mensaje Enviado con exito"
        contador += 1
        #mi_socket.flush()
        # mi_socket.recv(1500)
    print "Conexión: %d" % (contador)    

    #mi_socket.shutdown(1)    