from flask_restful import fields
from helper.database import db

atendimento_fields = {
    'id':   fields.Integer,
    'n':   fields.String,
    'nome':   fields.String,
    'nascimento': fields.String,
    'cns':   fields.String,
    'cpf':   fields.String,
    'unidade':   fields.String,
    'data_atendimento':   fields.String,
    'condicao_saude':   fields.String,
}


class Atendimento(db.Model):
    __tablename__ = "tb_atendimento"

    id = db.Column(db.Integer, primary_key=True)
    n = db.Column(db.String(255), unique=False, nullable=False)
    nome = db.Column(db.String(255), unique=False, nullable=False)
    nascimento = db.Column(db.String(255), unique=False, nullable=False)
    cns = db.Column(db.String(255), unique=False, nullable=False)
    cpf = db.Column(db.String(255), unique=False, nullable=False)
    unidade = db.Column(db.String(255), unique=False, nullable=False)
    data_atendimento = db.Column(db.String, nullable=False)
    condicao_saude = db.Column(db.String(255), unique=False, nullable=False)


    def __init__(self, n: str, nome: str, nascimento: str, cns: str, cpf: str, unidade: str, data_atendimento: str, condicao_saude: str):
        self.n = n
        self.nome = nome
        self.nascimento = nascimento
        self.cns = cns
        self.cpf = cpf
        self.unidade = unidade
        self.data_atendimento = data_atendimento
        self.condicao_saude = condicao_saude

    def __repr__(self) -> str:
        return f"""<Atendimento 
                        ID={self.id},
                        N={self.n},        
                        Nome={self.nome},
                        Nascimento={self.nascimento},
                        CNS={self.cns},
                        CPF={self.cpf},
                        Unidade={self.unidade},
                        Data_Atendimento = {self.data_atendimento},
                        Condicao_Saude = {self.condicao_saude}>"""
