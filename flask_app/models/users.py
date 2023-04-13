from flask_app.config.mysqlconnection import connectToMySQL

import re #importamos expresiones regulares
#crear una expresion regular para verificar que tengamos un email con el formato correcto

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
        result = connectToMySQL('muroprivado').quey_db(query, formulario)
        return result
    
    @staticmethod
    def valida_usuario(formulario):
        es_valido = True
        
        #validar que el nombre y el apellido tenga mas de 3 caracteres
        if len(formulario['first_name']) < 3:
            flash('Nombre debe de tener mas de 3 caracteres','registro')
            es_valido = False
        
        if len(formulario['last_name']) < 3:
            flash('Apellido debe de tener mas de 3 caracteres','registro')
            es_valido = False
        
        #validar email con expresiones regulares