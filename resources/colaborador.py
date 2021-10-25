from flask_restful import Resource, reqparse
from models.colaborador import ColaboradorModel



class Colaboradores(Resource):
    def get(self):
        return {"colaboradores" : [colaborador.json() for colaborador in ColaboradorModel.query.all()] }        

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
                
    def get(self, matricula):
        colaborador = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador:
                return colaborador.json()
        return {"message" : "Colaborador nao encontrado"}, 404

    def post(self, matricula):
        if ColaboradorModel.encontrar_colaborador(matricula):
            return {'message': 'Matricula "{}" ja existe!'.format(matricula)} , 400 # bad request!

        dados = Colaborador.argumentos.parse_args()
        colaborador = ColaboradorModel(matricula, **dados)
        colaborador.save_colaborador()
        return colaborador.json()


    # def put(self, matricula):

    #     dados = Colaborador.argumentos.parse_args()
    #     novo_colaborador = {"matricula" : matricula, **dados }
    #     # novo_colaborador_objeto = ColaboradorModel(matricula, **dados)
    #     # novo_colaborador = novo_colaborador_objeto.json()

    #     colaborador = Colaborador.encontrar_colaborador2(matricula)
    #     if colaborador:
    #         colaborador.update(novo_colaborador)
    #         return novo_colaborador, 200
    #     colaboradores.append(novo_colaborador)
    #     return novo_colaborador, 201 #criado!

    # def delete(self, matricula):
    #     global colaborador
    #     colaborador = [colaborador for colaborador in colaboradores if colaborador["matricula"] != matricula]
    #     return {"message" : "Colaborador deletado."}