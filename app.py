from flask import Flask, Blueprint
from helper.database import db, migrate
from helper.api import api, blueprint
from helper.cors import cors
import pandas as pd

app = Flask(__name__)
api.init_app(app)
cors.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:94X0kNnpftJ1@db-postgres:5432/pgdata"
db.init_app(app)
migrate.init_app(app, db)

atendimento_blueprint = Blueprint('atendimento', __name__)

@atendimento_blueprint.cli.command('load-csv')
def load_csv():
    # Carrega o CSV
    df = pd.read_csv('atendimentos.csv')

    # Adiciona cabeçalho à primeira coluna
    df.rename(columns={df.columns[0]: 'id'}, inplace=True)

    # Renomeia a segunda coluna
    df.rename(columns={df.columns[1]: 'n'}, inplace=True)

    # Formata os cabeçalhos para minúsculas
    df.columns = df.columns.str.lower()

    # Formata as datas para o formato YYYY-MM-DD
    def format_date(date_string):
        try:
            return pd.to_datetime(date_string).strftime('%Y-%m-%d')
        except ValueError:
            print(f"Erro ao converter a data: {date_string}")
            return None

    df['data_atendimento'] = df['data_atendimento'].apply(format_date)

    # Insere os dados no banco de dados
    with app.app_context():
        df.to_sql('tb_atendimento', con=db.engine, if_exists='append', index=False)
    
    print('Dados do CSV carregados com sucesso!')

app.register_blueprint(atendimento_blueprint)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=8001, host='0.0.0.0')
