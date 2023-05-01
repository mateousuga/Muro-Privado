from flask_app.config.mysqlconnection import connectToMySQL

import re #importamos expresiones regulares
#crear una expresion regular para verificar que tengamos un email con el formato correcto
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') #Expresion regular de email

from flask import flash #mandar mensajes a la plantilla

class User:
    
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO users(first_name, last_name, email, password) VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL('muroprivado').query_db(query, formulario)
        return result #regresamos el ID de nuestro usuario (result=identificador del nuevo registro) insert recibe ID
    
    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        #validar que el nombre y el apellido tenga mas de 3 caracteres
        if len(formulario['first_name']) < 3:
            flash('El nombre debe de tener mas de 3 caracteres','registro')
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash('El apellido debe de tener mas de 3 caracteres','registro')
            es_valido = False
        
        #validar email con expresiones regulares
        if not EMAIL_REGEX.match(formulario['email']):
            flash('Email invalido','registro')
            es_valido = False
        
        if len(formulario['password']) < 6:
            flash('La contraseña debe de tener como minimo 6 caracteres', 'registro')
            es_valido = False
        
        if formulario['password'] != formulario['confirm_password']:
            flash('Las contraseñas no conciden', 'registro')
            es_valido = False
        
        #consultar si ya existe el correo
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL('muroprivado').query_db(query, formulario)
        if len(results) >= 1:
            flash('El email ya esta registrado', 'registro')
            es_valido = False
        
        return es_valido
    
    @classmethod
    def get_by_email(cls, formulario):
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('muroprivado').query_db(query, formulario)
        if len(result) < 1:
            return False
        else:
            user = cls(result[0]) #haciendo una instancia de user con los datos recibidos de la base de datos
            return user
    
    @classmethod
    def get_by_id(cls, formulario):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('muroprivado').query_db(query, formulario) #select recibe una lista
        user = cls(result[0])
        return user