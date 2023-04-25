from flask import render_template, redirect, session, request, flash #importaciones de modulos de flask

from flask_app import app

#importanto modelo de user
from flask_app.models.users import User

#importar bcrypt (encriptar)

@app.route('/')
def index():
    return render_template('index.html')


#crear ruta para /register
@app.route('/register', methods=['POST'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    User.save(request.form)
    return redirect('/inicio.html')

@app.route('/inicio.html')
def inicio():
    return render_template('inicio.html')