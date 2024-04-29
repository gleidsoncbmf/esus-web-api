from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        return {'message': 'Desafio Prático: API REST para Acesso a Dados de Saúde'}

    