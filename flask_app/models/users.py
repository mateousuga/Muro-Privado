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