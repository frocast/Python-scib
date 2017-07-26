# -*- coding:utf-8 -*-
import socket
import os
import time

mi_socket=socket.socket()
mi_socket.connect(("http://medico-146102.appspot.com", 80))
contador = 0

os.system("clear")
tiempo_inicio = str(time.strftime("%X"))
#            print "Petición número: %d, Hora %s"  % (conexiones, tiempo)
try:
    while True:
        mensaje="t"
        if mi_socket.send(mensaje): 
            #print "Mensaje Enviado con exito"
            tiempo_final = str(time.strftime("%X"))
            contador += 1
            #mi_socket.flush()
            # mi_socket.recv(1500)
        #print "Conexión: %d" % (contador)    

        #mi_socket.shutdown(1)    
except:
    print "inicio: %s, tiempo termino: %s, numero de conexiones: %d" %(tiempo_inicio, tiempo_final, contador) 