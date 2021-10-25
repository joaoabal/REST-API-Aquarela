from flask_restful import Resource, reqparse
from models.colaborador import ColaboradorModel

colaboradores = [
    {
        "matricula" : "123",
       "nome" : "claudio",
       "sobrenome" : "raba",
       "cargo" : "gerente",
       "codigo_cargo" : "g2",
       "lider" : "alvaro",
       "matricula_lider" : "35497",
       "salario" : "2000",
       "senha" : "claudio123",
       "status_colaborador" : "contratado",
    },
]


class Colaboradores(Resource):
    def get(self):
        return {"colaboradores":colaboradores}

class Colaborador(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome")
    argumentos.add_argument("sobrenome")
    argumentos.add_argument("cargo")
    argumentos.add_argument("codigo_cargo")
    argumentos.add_argument("lider")
    argumentos.add_argument("matricula_lider")
    argumentos.add_argument("salario")
    argumentos.add_argument("senha")
    argumentos.add_argument("status_colaborador")

    def encontrar_colaborador(matricula):
        for colaborador in colaboradores:
            if colaborador["matricula"] == matricula:
                return colaborador
        return None
                
    def get(self, matricula):
        colaborador = Colaborador.encontrar_colaborador(matricula)
        if colaborador:
                return colaborador
        return {"message" : "Colaborador nao encontrado"}, 404

    def post(self, matricula):
        if ColaboradorModel.find_colaborador(matricula):
            return {'message': 'Matricula "{}" ja existe!'.format(matricula)} , 400 # bad request!

        dados = Colaborador.argumentos.parse_args()


        # novo_colaborador = {"matricula" : matricula, **dados }


        # colaboradores.append(novo_colaborador)
        # return novo_colaborador, 200

        novo_colaborador_objeto = ColaboradorModel(matricula, **dados)
        novo_colaborador = novo_colaborador_objeto.json()
        colaboradores.append(novo_colaborador)
        return novo_colaborador, 200

    def put(self, matricula):

        dados = Colaborador.argumentos.parse_args()
        novo_colaborador = {"matricula" : matricula, **dados }
        # novo_colaborador_objeto = ColaboradorModel(matricula, **dados)
        # novo_colaborador = novo_colaborador_objeto.json()

        colaborador = Colaborador.encontrar_colaborador(matricula)
        if colaborador:
            colaborador.update(novo_colaborador)
            return novo_colaborador, 200
        colaboradores.append(novo_colaborador)
        return novo_colaborador, 201 #criado!

    def delete(self, matricula):
        global colaborador
        colaborador = [colaborador for colaborador in colaboradores if colaborador["matricula"] != matricula]
        return {"message" : "Colaborador deletado."}