from flask_app import app

#importando controlador 
from flask_app.controllers import users_controller

if __name__ == "__main__":
    app.run(debug=True)