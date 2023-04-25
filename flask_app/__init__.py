from flask import Flask

app = Flask(__name__)

#Generar secret_key
app.secret_key = "llave_secreta"