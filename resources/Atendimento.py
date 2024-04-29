from flask_restful import Resource, marshal
from model.Atendimento import Atendimento, atendimento_fields
from webargs import fields
from webargs.flaskparser import use_kwargs
from sqlalchemy import and_

class AtendimentoResource(Resource):
    args = {
        'data_atendimento': fields.Str(required=False, missing=None),
        'condicao_saude': fields.Str(required=False, missing=None),
        'unidade': fields.Str(required=False, missing=None)
    }

    @use_kwargs(args, location="query")
    def get(self, **kwargs):
        filters = []
        for key, value in kwargs.items():
            if value is not None:
                filters.append(Atendimento.__table__.columns[key].ilike(f'%{value}%'))

        atendimentos = Atendimento.query.filter(and_(*filters)).all()

        if atendimentos:
            return marshal(atendimentos, atendimento_fields), 200
        return {'message': 'Nenhum atendimento encontrado para os filtros fornecidos'}, 404
