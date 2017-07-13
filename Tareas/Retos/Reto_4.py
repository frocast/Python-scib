from pymongo import MongoClient
from flask import Flask, render_template, request, redirect

cliente = MongoClient()
db = cliente.cic

app = Flask(__name__)

@app.route('/encuesta', methods=['GET','POST'])
def encuesta():
    if request.method == 'GET':
        return render_template("formulario.html", chk=False)

    gender = request.form["gender"]
    animals = request.form["animals"]
    music = request.form["music"]

    respuesta=db.encuestas.insert({
        "gender": gender,
        "animals": animals,
        "music": music
    })

    return render_template("formulario.html", chk=True)

if __name__ == "__main__":
    app.run()