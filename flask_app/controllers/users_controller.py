from flask import render_template, redirect, session, request, flash #importaciones de modulos de flask

from flask_app import app

#importanto modelo de user
from flask_app.models.users import User

#importar bcrypt (encriptar)
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) #inicializando instancia de Bcrypt

@app.route('/')
def index():
    return render_template('index.html')


#crear ruta para /register
@app.route('/register', methods=['POST'])
def register():
    if not User.valida_usuario(request.form):
        return redirect('/')
    
    pwd = bcrypt.generate_password_hash(request.form['password']) #Encripta la contraseña
    
    formulario = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }
    
    User.save(formulario)
    return redirect('/inicio.html')

@app.route('/inicio.html')
def inicio():
    return render_template('inicio.html')