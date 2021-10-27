from flask_restful import Resource, reqparse
from models.colaborador import ColaboradorModel

class Colaboradores(Resource):
    def get(self):
        return {"colaboradores" : [colaborador.json() for colaborador in ColaboradorModel.query.all()] }        

class Colaborador(Resource):

    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=False)
    argumentos.add_argument("sobrenome", type=str, required=False)
    argumentos.add_argument("cargo", type=str, required=False)
    argumentos.add_argument("codigo_cargo", type=str, required=False)
    argumentos.add_argument("lider", type=str, required=False)
    argumentos.add_argument("matricula_lider", type=str, required=False)
    argumentos.add_argument("salario", type=str, required=False)
    argumentos.add_argument("senha", type=str, required=False)
    argumentos.add_argument("status_colaborador", type=str, required=False)
                
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
        try:
            colaborador.save_colaborador()
        except:
            return {"message" : "Erro interno tentando salvar."} , 500 # internal server error
        return colaborador.json()

    def put(self, matricula):

        dados = Colaborador.argumentos.parse_args()

        colaborador_encontrado = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador_encontrado:
            colaborador_encontrado.update_colaborador(**dados)
            try:
                colaborador_encontrado.save_colaborador()
            except:
                return {"message" : "Erro interno tentando salvar."} , 500 # internal server error
            return colaborador_encontrado.json(), 200
        colaborador = ColaboradorModel(matricula, **dados)
        colaborador.save_colaborador()
        return colaborador.json(), 201 #criado!

    def delete(self, matricula):
        colaborador = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador:
            try:
                colaborador.delete_colaborador()
            except:
                return {"message" : "Erro interno tentando deletar."} , 500 # internal server error
            return {"message" : "Colaborador deletado."}
        return {"message" : "Colaborador não encontrado."} , 404

