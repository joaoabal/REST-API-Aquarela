from sql_alchemy import bd

class ColaboradorModel(bd.Model):
    __tablebane__ = "public.colaboradores"

    matricula = bd.Column(bd.String, primary_key = True)
    nome = bd.Column(bd.String)
    sobrenome = bd.Column(bd.String)
    cargo = bd.Column(bd.String)
    codigo_cargo = bd.Column(bd.String)
    lider = bd.Column(bd.String)
    matricula_lider = bd.Column(bd.String)
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

    def json(self):
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

    # def 
