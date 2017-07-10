##########################################################################################################

##########################################################################################################

from flask import Flask

app = Flask(__name__)

@app.route('/user/<nombre>')
def user(nombre):
    return "Hola %s" % nombre

app.run() #Configuracion de puerto app.run(Port=3000)
