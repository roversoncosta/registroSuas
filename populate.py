from app.models import *
from importFromDrive import importAcoes, importEventos, importInsterset
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
    csv_data = importAcoes.importAcoes() # dados dos registros
    # csv_data.to_csv('test_data.csv', index=False)
    dic_nome_email = dict(csv_data.groupby(['nome_profissional','email']).size().reset_index().drop(columns=[0]).values)
    csv_data['email'] = csv_data['nome_profissional'].map(dic_nome_email) # preenche email vazios baseados nos emais ja resgitrados
    data = pd.merge(csv_data, df_users, how='left', left_on='email', right_on='email' )
    data['id'] = pd.to_numeric(data['id'],errors='coerce').astype('Int8')

    data = data.drop(columns=['email','nome_profissional','data_publicacao']).copy()
    data['n_profissionais_atendidos'] = data['n_profissionais_atendidos'].astype('int8')
    data['data_acao'] = pd.to_datetime(data['data_acao'], errors='coerce')
    # aqui  filtra o tipo de acao, seleciona o model de acordo com a acao
    # data = data.loc[data['acao_realizada']=='Apoio Técnico Presencial (ATP)']
    # data = data.loc[data['acao_realizada']=='Apoio Técnico Não Presencial (ATNP)']
    data = data.loc[data['acao_realizada']=='Outras Ações']
    # print(data.data_acao)
    df_records = data.to_dict('records')
    model_instances = [AcaoOutrasModel(
        acao_realizada = record['acao_realizada'],
        caracteristica_acao =record['caracteristica_acao'],
        n_profissionais_atendidos = record['n_profissionais_atendidos'],
        descricao_acao = record['descricao_acao'],
        data_acao = record['data_acao'],
        municipio_atendido = record['municipio_atendido'],
        user_id = record['id'],
        )   for record in df_records]

    AcaoOutrasModel.objects.bulk_create(model_instances)


## REGISTRO EM MASSA DE EVENTOS
def bulk_create_eventos():
    df_users = pd.DataFrame(list(User.objects.all().values('email','id'))) # dados dos usuarios 
    # df_users.to_csv('test_users.csv', index=False)   
    csv_data = importEventos.importEventos() # dados dos registros
    # csv_data.to_csv('test_data.csv', index=False)
    data = pd.merge(csv_data, df_users, how='left', left_on='email', right_on='email' )
    print(data.info())
    data = data.drop(columns=['email','nome_profissional','setor']).copy()
    data['data_inicial'] = pd.to_datetime(data['data_inicial'], errors='coerce')
    data['data_final'] = pd.to_datetime(data['data_final'], errors='coerce')
    # print(data.info())
    df_records = data.to_dict('records')
    model_instances = [TableEventModel(
        titulo_evento = record['titulo_evento'],
        tipo_evento =record['tipo_evento'],
        data_inicial =record['data_inicial'],
        data_final =record['data_final'],
        instituicao_ofertante = record['instituicao_ofertante'],
        descricao_evento = record['descricao_evento'],
        user_id = record['id'],
        )   for record in df_records]

    TableEventModel.objects.bulk_create(model_instances)

## REGISTRO EM MASSA DE EVENTOS
def bulk_create_interset():
    df_users = pd.DataFrame(list(User.objects.all().values('email','id'))) # dados dos usuarios
    csv_data = importInsterset.importInterset() # dados dos registros
    data = pd.merge(csv_data, df_users, how='left', left_on='email', right_on='email' )
    data = data.drop(columns=['email']).copy()
    data['data_participacao'] = pd.to_datetime(data['data_participacao'], errors='coerce')
    # print(data.info())
    df_records = data.to_dict('records')
    model_instances = [TableIntersetModel(
        espaco_participacao_suas=record['espaco_participacao_suas'],
        espaco_participacao_intersetoriais=record['espaco_participacao_intersetoriais'],
        data_participacao =record['data_participacao'],
        local = record['local'],
        descricao = record['descricao'],
        encaminhamentos = record['encaminhamentos'],
        user_id = record['id'],
        )   for record in df_records]

    TableIntersetModel.objects.bulk_create(model_instances)

# RODAR FUNCOES
# bulk_create_users() 
# bulk_create_acoes()
# bulk_create_eventos()
# bulk_create_interset()