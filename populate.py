from app.models import AcaoAtpModel,AcaoAtnpModel,AcaoOutrasModel, User
from importFromDrive import importData
import pandas as pd

def populate_data():
    df = pd.read_csv('file.csv', sep=';', encoding='latin-1', parse_dates=['data_acao','data_publicacao'])
    print(df.head())
    df_records = df.to_dict('records')
    model_instances = [AcaoAtpModel(
        acao_realizada = record['acao_realizada'],
        caracteristica_acao =record['caracteristica_acao'],
        n_profissionais_atendidos = record['n_profissionais_atendidos'],
        descricao_acao = record['descricao_acao'],
        data_acao = record['data_acao'],
        data_publicacao = record['data_publicacao'],
        municipio_atendido = record['municipio_atendido'],
        user_id = record['user_id'],
        )   for record in df_records]

    AcaoAtpModel.objects.bulk_create(model_instances)

    # AcaoAtpModel.objets.filter(user_id=1).delete()
    ## Insert data into Model
    # Para rodar um codigo python usando o shell:python manage.py shell <importing.py

def populate_acoes():
    # importa dados dos usuários registrados
    df_users = pd.DataFrame(list(User.objects.all().values()))
    # Importa dados do RU diretamente do google grive
    df_ru_from_drive = importData.importAcoes()
    ## Pega os 'id' dos usuários registrados e cria uma coluna 'id' na base do ru importada do drive para ser usado para inserir os dados baseados no numero do id
    data = df_ru_from_drive.merge(df_users[['email','id']], how='left', left_on='email', right_on='email' )
    data.id = pd.to_numeric(data.id, errors='coerce').astype('Int64')
    ### ate aqui em cima está ok. verificar loop que insira os valores baseados por Models e por idss
    list_action_models = [AcaoAtpModel,AcaoAtnpModel,AcaoOutrasModel]
    for model in list_action_models:
        if id == data['id'].values:
            df_records = df_ru_from_drive.to_dict('records')
            model_instances = [model(
                acao_realizada = record['acao_realizada'],
                caracteristica_acao =record['caracteristica_acao'],
                n_profissionais_atendidos = record['n_profissionais_atendidos'],
                descricao_acao = record['descricao_acao'],
                data_acao = record['data_acao'],
                data_publicacao = record['data_publicacao'],
                municipio_atendido = record['municipio_atendido'],
                user_id = record['user_id'],)   for record in df_records]

    AcaoAtpModel.objects.bulk_create(model_instances)

# populate_data()



def test_data():
    df_users = pd.DataFrame(list(User.objects.all().values())) # dados dos usuarios 
    df_users.to_csv('df_users.csv', index=False)   

    data = importData.importAcoes() # dados dos registros
    data.to_csv('data_test.csv', index=False)

    data = pd.merge(data, df_users[['email','id']], how='left', left_on='email', right_on='email' )
    # data['id'] = data['id'].astype(int)

    data = data.loc[data['acao_realizada']=='Apoio Técnico Presencial (ATP)']
    data = data.drop(columns=['email','nome_profissional','data_publicacao']).copy()
    data['n_profissionais_atendidos'] = data['n_profissionais_atendidos'].astype(int)
    # data = data.iloc[0:1,:]

    # df_records = data.to_dict('records')
    # print(df_records)
    # model_instances = [AcaoAtpModel(
    #     acao_realizada = record['acao_realizada'],
    #     caracteristica_acao =record['caracteristica_acao'],
    #     n_profissionais_atendidos = record['n_profissionais_atendidos'],
    #     descricao_acao = record['descricao_acao'],
    #     data_acao = record['data_acao'],
    #     # data_publicacao = record['data_publicacao'],
    #     municipio_atendido = record['municipio_atendido'],
    #     user_id = 1,
    #     )   for record in df_records]

    # AcaoAtpModel.objects.bulk_create(model_instances)
test_data()