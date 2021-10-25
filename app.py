# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 18:26:00 2021

@author: João Abal
"""

from flask import Flask
from flask_restful import Api
from resources.colaborador import Colaboradores
from resources.colaborador import Colaborador

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5001/dbteste2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

@app.before_first_request
def cria_db():
    bd.create_all()


api.add_resource(Colaboradores,"/colaborador")
api.add_resource(Colaborador,"/colaborador/<string:matricula>")

if __name__ == "__main__":
    from sql_alchemy import bd
    bd.init_app(app) #garante que o banco seja executado somente por esse arquivo
    app.run(debug=True)