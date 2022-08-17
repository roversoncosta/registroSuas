# from app.models import User
# import pandas as pd

# df = pd.read_csv('file.csv', sep=';', encoding='latin-1', parse_dates=['data_acao','data_publicacao'])
# print(df.info())

# df_records = df.to_dict('records')
# print('Dataframde to dictionary......OK!')
# model_instances = [AcaoAtpModel(
#     # id=record['id'],
#     acao_realizada = record['acao_realizada'],
#     caracteristica_acao =record['caracteristica_acao'],
#     n_profissionais_atendidos = record['n_profissionais_atendidos'],
#     descricao_acao = record['descricao_acao'],
#     data_acao = record['data_acao'],
#     data_publicacao = record['data_publicacao'],
#     municipio_atendido = record['municipio_atendido'],
#     user_id = record['user_id'],)  
    
#     for record in df_records]

# print('Create Model Instance......OK!')

# # ### como deletar todas os registros baseados em um user_id:
# AcaoAtpModel.objects.filter(user_id=1).delete()
# print('Delete all regiter by user_id=1......OK!')
# ## Insert data into Model
# AcaoAtpModel.objects.bulk_create(model_instances)
# print('Data inserted into Model......OK!')
# print('Finished!')
# # Para rodar um codigo python usando o shell:
# # python manage.py shell <importing.py