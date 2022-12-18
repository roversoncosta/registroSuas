from app.models import AcaoAtpModel,AcaoAtnpModel,AcaoOutrasModel, User
from importFromDrive import importData
from django.contrib.auth.hashers import make_password

import pandas as pd

### REGISTRO EM MASSA DE USUARIOS
def bulk_create_users():
    df = pd.read_csv('users.csv',sep=';')
    df_records = df.to_dict('records')
    model_instances = [User(
        username = record['username'],
        first_name =record['first_name'],
        last_name = record['last_name'],
        email = record['email'],
        password = make_password(record['password1']),
        # password2 = record['password2'],
        sector_name = record['sector_name']
        )  for record in df_records ]
    User.objects.bulk_create(model_instances)
    
## REGISTRO EM MASSA DE ACOES 
def bulk_create_acoes():
    df_users = pd.DataFrame(list(User.objects.all().values('email','id'))) # dados dos usuarios 
    # df_users.to_csv('test_users.csv', index=False)   
    csv_data = importData.importAcoes() # dados dos registros
    # csv_data.to_csv('test_data.csv', index=False)
    dic_nome_email = dict(csv_data.groupby(['nome_profissional','email']).size().reset_index().drop(columns=[0]).values)
    csv_data['email'] = csv_data['nome_profissional'].map(dic_nome_email) # preenche email vazios baseados nos emais ja resgitrados
    data = pd.merge(csv_data, df_users, how='left', left_on='email', right_on='email' )
    data['id'] = pd.to_numeric(data['id'],errors='coerce').astype('Int8')

    data = data.drop(columns=['email','nome_profissional','data_publicacao']).copy()
    data['n_profissionais_atendidos'] = data['n_profissionais_atendidos'].astype('int8')
    data['data_acao'] = pd.to_datetime(data['data_acao'], errors='coerce')
    # aqui  filtra o tipo de acao, seleciona o model de acordo com a acao
    data_atp = data.loc[data['acao_realizada']=='Apoio Técnico Presencial (ATP)']
    # data_atnp = data.loc[data['acao_realizada']=='Apoio Técnico Não Presencial (ATNP)']
    # data_outras = data.loc[data['acao_realizada']=='Outras Ações']
    # print(data_atp.data_acao)
    df_records = data_atp.to_dict('records')
    model_instances = [AcaoAtpModel(
        acao_realizada = record['acao_realizada'],
        caracteristica_acao =record['caracteristica_acao'],
        n_profissionais_atendidos = record['n_profissionais_atendidos'],
        descricao_acao = record['descricao_acao'],
        data_acao = record['data_acao'],
        municipio_atendido = record['municipio_atendido'],
        user_id = record['id'],
        )   for record in df_records]

    AcaoAtpModel.objects.bulk_create(model_instances)

# RODAR FUNCOES
# bulk_create_users() 
bulk_create_acoes()