# -*- coding:utf-8 -*-
import os
import time
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import HTTPError as BaseHTTPError

os.system("clear")
conexiones = 0
tiempo = ""

try:
    # req = requests.get('https://www.google.com')
    # print req.ok
    # soup = BeautifulSoup(req.text, "html5lib")
    # print soup
    while True: 
        solicitud = requests.get('http://www.sepi.esimez.ipn.mx')
        if solicitud.ok:
            soup = BeautifulSoup(solicitud.text, "lxml")
            tiempo = str(time.strftime("%X"))
            print "Petición número: %d, Hora %s"  % (conexiones, tiempo)
            conexiones += 1

except requests.exceptions.SSLError:
    print "Error con el certificado SSL"

except: 
    print "Se tuvieron %d conexiones exitosas en %s" % (conexiones,tiempo )