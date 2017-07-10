from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

cliente = MongoClient()
db = cliente.cic

app = Flask(__name__)
app.secret_key = 'Clave_Secreta_Flask_Session'

#@app.route('/<nombre_py>')
#def home(nombre_py):
#    return render_template("index.html", nombre_html=nombre_py)

@app.route('/')
def home():
    if "usuario" in session:
        return render_template("index.html", nombre = session['usuario'])

    return redirect("/login")
   
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    usuario = request.form["usuario"]
    clave = request.form["clave"]

    usuariodb = db.usuarios.find_one({
        "usuario":usuario,
        "clave":clave
    })

    if not usuariodb:
        return render_template("/login.html", error=True)

    session['usuario'] = usuariodb["usuario"]

    return redirect("/")

@app.route('/logout')
def logout():
    
    session.pop('usuario', None)
    return redirect('/')


app.run()