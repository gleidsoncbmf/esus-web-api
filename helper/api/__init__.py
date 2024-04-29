from flask import Blueprint
from flask_restful import Api

from resources.Atendimento import AtendimentoResource
from resources.Index import IndexResource


blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api/v1")

api.add_resource(IndexResource, '/')

api.add_resource(AtendimentoResource, '/atendimentos')


