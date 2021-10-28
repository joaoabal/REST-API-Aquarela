# -*- coding: utf-8 -*-
"""
Desafio Backend Aquarela
@author: João Abal
25/10/2021
"""

from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from resources.colaborador import Colaboradores, Colaborador

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5001/dbteste"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)
cors = CORS(app)

@app.before_first_request
def cria_db():
    bd.create_all()

api.add_resource(Colaboradores,"/colaborador")
api.add_resource(Colaborador,"/colaborador/<string:matricula>")

if __name__ == "__main__":
    from sql_alchemy import bd
    bd.init_app(app)
    app.run(debug=True)