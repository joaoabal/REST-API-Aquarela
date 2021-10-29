'''
app.TDD trata de realização de testes unitários de funcionalidades básicas da API:
TestModel: cls
    Teste de Classe modelo construção de atributos.
TestApi: cls
    Teste de conexão com banco de dados, post e get.
'''

import unittest
from app import app
from flask_sqlalchemy import SQLAlchemy
from models.colaborador import ColaboradorModel
from resources.colaborador import Colaborador, Colaboradores

class TestModel(unittest.TestCase):
    '''
    Classe unittest para teste da construção de atributos pela classe modelo ColaboradorModel.
    
    Métodos
    -------
    setUp()
        inicializa os atributos do teste
    test_import()
        teste de construção dos atributos
    '''

    def setUp(self):

        self.colaborador_1 = ColaboradorModel("123","Jose","Souza","Diretor","597","Claudio","Diretor_2", "2000", "minhasenha","contratado")
        self.colaborador_2 = ColaboradorModel("1234","Gilson","Souza","Diretor_2","597","Claudio","Diretor", "2000", "minhasenha","contratado")

    def test_import(self):

        self.assertEqual(self.colaborador_1.matricula, '123')
        self.assertEqual(self.colaborador_1.nome, 'Jose')
        self.assertEqual(self.colaborador_1.sobrenome, 'Souza')
        self.assertEqual(self.colaborador_1.cargo, 'Diretor')
        self.assertEqual(self.colaborador_1.codigo_cargo, '597')
        self.assertEqual(self.colaborador_1.lider, 'Claudio')
        self.assertEqual(self.colaborador_1.matricula_lider, 'Diretor_2')
        self.assertEqual(self.colaborador_1.salario, '2000')
        self.assertEqual(self.colaborador_1.senha, 'minhasenha')
        self.assertEqual(self.colaborador_1.status_colaborador, 'contratado')
  
        self.assertEqual(self.colaborador_2.matricula, '1234')
        self.assertEqual(self.colaborador_2.nome, 'Gilson')
        self.assertEqual(self.colaborador_2.sobrenome, 'Souza')
        self.assertEqual(self.colaborador_2.cargo, 'Diretor_2')
        self.assertEqual(self.colaborador_2.codigo_cargo, '597')
        self.assertEqual(self.colaborador_2.lider, 'Claudio')
        self.assertEqual(self.colaborador_2.matricula_lider, 'Diretor')
        self.assertEqual(self.colaborador_2.salario, '2000')
        self.assertEqual(self.colaborador_2.senha, 'minhasenha')
        self.assertEqual(self.colaborador_2.status_colaborador, 'contratado')

class TestApi(unittest.TestCase):
    '''
    Classe unittest para teste da API.
    
    Métodos
    -------
    setUp()
        inicializa os atributos do teste
            app : aplicação
            bd : banco de dados
            matricula_teste : matricula inicial para teste
    tearDown()
        encerra os atributos do teste
    test_postEget()
        salva matricula no banco e confere por query se a mesma foi salva com sucesso
    '''

    def setUp(self):

        app.config["TESTING"] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5001/dbteste"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        self.app = app.test_client()

        self.bd = SQLAlchemy(app)
        self.bd.create_all()
        self.bd.init_app(app)

        while (True):
            self.matricula_teste = input("Entre com a matrícula de teste:\n")
            if (self.bd.session.query(ColaboradorModel).filter_by(matricula=self.matricula_teste).first()):
                print("Tente uma matrícula que ainda não existe!")
            else:
                break

    def tearDown(self):

        self.bd.session.remove()
        self.bd.drop_all()

    def test_postEget(self):
            
        u = ColaboradorModel(matricula = self.matricula_teste, nome = "", sobrenome = "", 
            cargo= "", codigo_cargo= "", lider= "", matricula_lider= "", salario= "", senha= "", status_colaborador= "")

        self.bd.session.add(u)
        self.bd.session.commit()
        
        query_result = self.bd.session.query(ColaboradorModel).filter_by(matricula=self.matricula_teste).first()
        self.assertEqual(query_result.matricula, self.matricula_teste)
            

if __name__ == '__main__':
    unittest.main()