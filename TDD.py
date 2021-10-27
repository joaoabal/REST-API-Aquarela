import unittest
from unittest.mock import patch
from models.colaborador import ColaboradorModel
from resources.colaborador import Colaboradores
from resources.colaborador import Colaborador
import requests

class TestModel(unittest.TestCase):

    def setUp(self):
        self.colaborador_1 = ColaboradorModel("123","Jose","Souza","Diretor","597","Claudio","Diretor_2", "2000", "minhasenha","contratado")
        self.colaborador_2 = ColaboradorModel("1234","Gilson","Souza","Diretor_2","597","Claudio","Diretor", "2000", "minhasenha","contratado")


    # def tearDown(self):
    #     pass

    def test_import(self):
 
        self.assertEqual(self.colaborador_1.nome, 'Jose')
        self.assertEqual(self.colaborador_1.sobrenome, 'Souza')
        self.assertEqual(self.colaborador_1.matricula, '123')
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


class TestConnection(unittest.TestCase):

    def setUp(self):
        self.response = requests.get(f'http://localhost:5000/colaborador')

    def test_app(self):
        if self.response.ok:
            # print(self.response.text)
            return self.response.text
        else:
            return "Bad Response!"


class TestGet(unittest.TestCase):

    def setUp(self):
        self.colaborador_1 = ColaboradorModel("123","Jose","Souza","Diretor","597","Claudio","Diretor_2", "2000", "minhasenha","contratado")
    #     self.response = requests.get(f'http://localhost:5000/colaborador/%s'%self.colaborador_1.matricula)

    def test_post(self):
        with patch("Colaborador.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = True

            mocked_get.assert_called_with("http://localhost:5000/colaborador/%s"%self.colaborador_1.matricula)

            self.assertEqual(Colaborador.post(self, self.colaborador_1.matricula), self.response)






    # def test_get(self):
    #     if self.response.ok:
    #         self.assertEqual(Colaboradores.get(), self.response.text)
    #         return self.response.text
    #     else:
    #         return "Bad Response!"





# class TestGet(unittest.TestCase):

#      def setUp(self):
#         self.colaborador_1 = ColaboradorModel("123","Jose","Souza","Diretor","597","Claudio","Diretor_2", "2000", "minhasenha","contratado")
#         self.colaborador_2 = ColaboradorModel("1234","Gilson","Souza","Diretor_2","597","Claudio","Diretor", "2000", "minhasenha","contratado")




#     def test_get(self):
#         self.assertEqual('foo'.upper(), 'FOO')


#     # def test_get(self):
#     #     self.assertEqual('foo'.upper(), 'FOO')

#     # def test_isupper(self):
#     #     self.assertTrue('FOO'.isupper())
#     #     self.assertFalse('Foo'.isupper())

#     # def test_split(self):
#     #     s = 'hello world'
#     #     self.assertEqual(s.split(), ['hello', 'world'])
#     #     # check that s.split fails when the separator is not a string
#     #     with self.assertRaises(TypeError):
#     #         s.split(2)



if __name__ == '__main__':
    unittest.main()