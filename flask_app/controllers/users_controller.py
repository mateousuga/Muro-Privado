from flask import render_template, redirect, session, request, flash #importaciones de modulos de flask

from flask_app import app

#importanto modelo de user


#importar bcrypt (encriptar)

@app.route('/')
def index():
    return render_template('index.html')


#crear ruta para /register
