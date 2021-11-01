from flask_restful import Resource, reqparse
from models.colaborador import ColaboradorModel

class Colaboradores(Resource):
    '''Classe Recurso (/colaborador) com método get

    Métodos
    -------
    get()
        retorna todos os colaboradores salvos no banco de dados.
    '''
    def get(self):
        '''Método get da Classe Resource (/colaborador) que retorna todos os colaboradores salvos no banco de dados'''
        
        try:
            return {"colaboradores" : [colaborador.json() for colaborador in ColaboradorModel.query.all()]}   
        except:
            return {"mensagem" : "Colaboradores nao encontrados.", "codigo" : 500} , 500 

class Colaborador(Resource):
    '''Classe Recurso (/colaborador/<string:matricula>) que organiza API através da matrícula (Primary Key)

    Atributos
    ----------
    argumentos : objeto reqparse
        objeto que recebe os elementos da requisição
    argumentos.parse_args() : dict
        construtor com chave e valor de todos elementos da requisição
    matricula : str
        matricula (Primary Key) do colaborador
    nome : str, requerido
        nome do colaborador
    sobrenome : str, requerido
        sobrenome do colaborador
    cargo : str, opcional
        cargo do colaborador
    codigo_cargo : str, opcional
        codigo_cargo do colaborador
    lider : str, opcional
        lider do colaborador
    matricula_lider : str, opcional
        matricula_lider do colaborador
    salario : str, opcional
        salario do colaborador
    senha : str, opcional
        senha do colaborador
    status_colaborador : str, opcional
        status_colaborador do colaborador

    Métodos
    -------
    get(matricula)
        retorna o colaborador correspondente a matrícula de entrada.
    post(matricula)
        salva o colaborador correspondente a matrícula de entrada.
    put(matricula)
        atualza o colaborador ou salva novo colaborador correspondente a matrícula de entrada.
    delete(matricula)
        deleta o colaborador correspondente a matrícula de entrada.
    '''
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str, required=True)
    argumentos.add_argument("sobrenome", type=str, required=True)
    argumentos.add_argument("cargo", type=str, required=False)
    argumentos.add_argument("codigo_cargo", type=str, required=False)
    argumentos.add_argument("lider", type=str, required=False)
    argumentos.add_argument("matricula_lider", type=str, required=False)
    argumentos.add_argument("salario", type=str, required=False)
    argumentos.add_argument("senha", type=str, required=False)
    argumentos.add_argument("status_colaborador", type=str, required=False)
                
    def get(self, matricula):
        '''Método get da Classe Resource (/colaborador/<string:matricula>) que retorna o colaborador correspondente a matrícula de entrada '''
        
        colaborador = ColaboradorModel.encontrar_colaborador(matricula)
        if colaborador:
                return colaborador.json()
        return {"mensagem" : "Colaborador nao encontrado" , "codigo" : 404}, 404

    def post(self, matricula):
        '''Método post da Classe Resource (/colaborador/<string:matricula>) que salva o colaborador correspondente a matrícula de entrada '''
        
        if ColaboradorModel.encontrar_colaborador(matricula):
            return {'mensagem': "Matricula {} ja existe!".format(matricula) , "codigo" : 400} , 400

        try:
            dados = Colaborador.argumentos.parse_args()
        except:
            return {"mensagem" : "Nome/Sobrenome incompletos." , "codigo" : 401} , 401
        colaborador = ColaboradorModel(matricula, **dados)
        try:
            colaborador.salvar_colaborador()
        except:
            return {"mensagem" : "Erro interno tentando salvar." , "codigo" : 500} , 500
        return colaborador.json()

    def put(self, matricula):
        '''Método put da Classe Resource (/colaborador/<string:matricula>) que atualza colaborador ou salva novo colaborador correspondente a matrícula de entrada'''
        
        self.argumentos.replace_argument("nome", type=str, required=False)
        self.argumentos.replace_argument("sobrenome", type=str, required=False)
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



