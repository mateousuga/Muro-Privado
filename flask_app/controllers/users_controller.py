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


@app.route('/inicio')
def inicio():
    return render_template('inicio.html')

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
    
    id = User.save(formulario) #guardando al usuario y recibiendo el ID del nuevo registro
    session['user_id'] = id #guardando en session el identificador
    
    return redirect('/dashboard')


@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user: #si user=false
        flash('El email es incorreto', 'login')
        return redirect('/inicio')
    
    #comparacion de la contraseña encriptada con la del login
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('La contraseña es incorrecta', 'login')
        return redirect('/inicio')
    
    session['user_id'] = user.id
    
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/inicio')
    
    formulario = {
        "id": session['user_id'],
    }
    user = User.get_by_id(formulario)
    
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/inicio')  