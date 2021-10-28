from flask_restful import Resource, reqparse
from models.colaborador import ColaboradorModel

class Colaboradores(Resource):
    '''Classe Resource (/colaborador) com método get'''
    def get(self):
        '''Método get da Classe Resource (/colaborador) que retorna todos os colaboradores salvos no banco de dados'''
        try:
            return {"colaboradores" : [colaborador.json() for colaborador in ColaboradorModel.query.all()]}   
        except:
            return {"mensagem" : "Colaboradores nao encontrados.", "codigo" : 500} , 500 

class Colaborador(Resource):
    '''Classe Resource (/colaborador/<string:matricula>) que organiza API através da matrícula (Primary Key)
    
    Classe com os seguintes métodos:
    - get(self, matricula)
    - post(self, matricula)
    - put(self, matricula)
    - delete(self, matricula)
    '''
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
        '''Método get da Classe Resource (/colaborador/<string:matricula>) que retorna o colaborador correspondente a matrícula de entrada'''
        colaborador = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador:
                return colaborador.json()
        return {"mensagem" : "Colaborador nao encontrado" , "codigo" : 404}, 404

    def post(self, matricula):
        '''Método post da Classe Resource (/colaborador/<string:matricula>) que salva o colaborador correspondente a matrícula de entrada'''
        if ColaboradorModel.encontrar_colaborador(matricula):
            return {'mensagem': "Matricula {} ja existe!".format(matricula) , "codigo" : 400} , 400

        dados = Colaborador.argumentos.parse_args()
        colaborador = ColaboradorModel(matricula, **dados)
        try:
            colaborador.salvar_colaborador()
        except:
            return {"mensagem" : "Erro interno tentando salvar." , "codigo" : 500} , 500
        return colaborador.json()

    def put(self, matricula):
        '''Método put da Classe Resource (/colaborador/<string:matricula>) que atualza colaborador ou salva novo colaborador correspondente a matrícula de entrada'''
        dados = Colaborador.argumentos.parse_args()

        colaborador_encontrado = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador_encontrado:
            colaborador_encontrado.atualizar_colaborador(**dados)
            try:
                colaborador_encontrado.salvar_colaborador()
            except:
                return {"mensagem" : "Erro interno tentando salvar.", "codigo" : 500} , 500
            return colaborador_encontrado.json(), 200
        colaborador = ColaboradorModel(matricula, **dados)
        colaborador.salvar_colaborador()
        return colaborador.json(), 201 #criado!

    def delete(self, matricula):
        '''Método delete da Classe Resource (/colaborador/<string:matricula>) que deleta o colaborador correspondente a matrícula de entrada'''
        colaborador = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador:
            try:
                colaborador.deletar_colaborador()
            except:
                return {"mensagem" : "Erro interno tentando deletar.", "codigo" : 500} , 500
            return colaborador.json(), 200
        return {"mensagem" : "Colaborador não encontrado." , "codigo" : 404} , 404



