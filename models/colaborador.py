from sql_alchemy import bd

class ColaboradorModel(bd.Model):
    '''Classe Modelo que recebe o banco de dados e organiza a manipulação dos dados.
    
    Classe com os seguintes métodos de classe:
    - encontrar_colaborador(cls, matricula)
    Classe com os seguintes métodos:
    - salvar_colaborador(self)
    - atualizar_colaborador(self, nome, sobrenome, cargo, codigo_cargo, lider, matricula_lider, salario, senha, status_colaborador)
    - deletar_colaborador(self)
    - json(self)
    '''
    __tablename__ = "public.colaboradores"

    matricula = bd.Column(bd.String, primary_key = True)
    nome = bd.Column(bd.String)
    sobrenome = bd.Column(bd.String)
    cargo = bd.Column(bd.String)
    codigo_cargo = bd.Column(bd.String)
    lider = bd.Column(bd.String)
    matricula_lider = bd.Column(bd.String)
    salario = bd.Column(bd.String)
    senha = bd.Column(bd.String)
    status_colaborador = bd.Column(bd.String)

    def __init__(self, matricula, nome, sobrenome, cargo, codigo_cargo, lider, matricula_lider, salario, senha, status_colaborador):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.cargo = cargo
        self.codigo_cargo = codigo_cargo
        self.lider = lider
        self.matricula_lider = matricula_lider
        self.salario = salario
        self.senha = senha
        self.status_colaborador = status_colaborador

    @classmethod
    def encontrar_colaborador(cls, matricula):
        '''
        Método de classe que filtra o banco de acordo com a matricula de entrada para saber se a matricula já existe

        Se a matricula não existe, a função retorna None
        Se a matricula já existe, a função retorna o objeto colaborador
        '''   
        colaborador = cls.query.filter_by(matricula=matricula).first() # SELECT * FROM colaboradores WHERE matricula = matricula
        if colaborador:
            return colaborador
        return None

    def salvar_colaborador(self):
        '''Método que salva o colaborador no banco de dados'''   
        bd.session.add(self)
        bd.session.commit()

    def atualizar_colaborador(self, nome, sobrenome, cargo, codigo_cargo, lider, matricula_lider, salario, senha, status_colaborador):
        '''Método que atualiza os dados do colaborador sem apagar os dados atuais que não foram atualizados nessa requisição'''   
        if not nome == None:
            self.nome = nome
        if not sobrenome == None:    
            self.sobrenome = sobrenome
        if not cargo == None:
            self.cargo = cargo
        if not codigo_cargo == None:    
            self.codigo_cargo = codigo_cargo
        if not lider == None:
            self.lider = lider
        if not matricula_lider == None:
            self.matricula_lider = matricula_lider
        if not salario == None:
            self.salario = salario
        if not senha == None:
            self.senha = senha
        if not status_colaborador == None:
            self.status_colaborador = status_colaborador

    def deletar_colaborador(self):
        '''Método que deleta o colaborador do banco de dados'''   
        bd.session.delete(self)
        bd.session.commit()

    def json(self):
        '''Método que organiza os dados de entrada em formato JSON'''
        return {"matricula" : self.matricula,
            "nome" : self.nome,
            "sobrenome" : self.sobrenome,
            "cargo" : self.cargo,
            "codigo_cargo" : self.codigo_cargo,
            "lider" : self.lider,
            "matricula_lider" : self.matricula_lider,
            "salario" : self.salario,
            "senha" : self.senha,
            "status_colaborador" : self.status_colaborador}