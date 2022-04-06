import imp
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

# Singleton
db = SQLAlchemy() 

def init_app(app: Flask):
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = os.getenv("DATABASE_URI")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app) 

    
    # tudo pode ser transformado em objeto:
    app.db = db 


    # tudo pode ser transformado em objeto exemplo abaixo:
    # app.batata = 'Batata'
    # print(f'{app.batata=}')

    from app.models.call_record_model import CallRecord 

# AQUI A MIGRATION SUBSTITUI
    # db.create_all(app=app) 