import pandas as pd
def importAcoes():
    link_registros ='https://docs.google.com/spreadsheets/d/e/2PACX-1vSSSzbKEW5XI8PKTj9mueR1cGi_GlTeUOmWVYIm9-i-zbCoZpelscZv_YSj4MXVcf4kN-_VY0AFpNDm/pub?gid=1021085548&single=true&output=csv'
    reg = pd.read_csv(link_registros)
    df_acoes = reg[['Carimbo de data/hora','DATA:','PROFISSIONAL:','email','SETOR','MUNICÍPIO','AÇÃO REALIZADA:',
        '1.Apoio Técnico Presencial (ATP)','1.1 - Nº de profissionais atendidos(ATP)','1.2 - Descrição da Ação (ATP)',
        '2.Apoio Técnico Não Presencial (ATNP)','2.1 - Nº de profissionais atendidos(ATNP)','2.2 - Descrição da Ação (ATNP)',
        '3.Outras Ações','3.1 - Nº de profissionais atendidos (Outras ações)','3.2 - Descrição da Ação (Outras)'
        ]].copy()
    df_acoes = df_acoes.rename(columns={'Carimbo de data/hora':'data_publicacao','DATA:':'data_acao','PROFISSIONAL:':'nome_profissional','SETOR':'sector_name','MUNICÍPIO':'municipio_atendido'})
    
    ### Altera o nome de alguams colunas
    dic_acao = {'1.Apoio Técnico Presencial (ATP)': 'Apoio Tecnico Presencial (ATP)',
    '2.Apoio Técnico Não Presencial (ATNP)':'Apoio Tecnico Não Presencial (ATNP)',
    '3.Outras Ações': 'Outras Ações'}
    df_acoes['acao_realizada'] = df_acoes['AÇÃO REALIZADA:'].map(dic_acao)

    ### NOVA COLUNA 1 - Cria a coluna 'caracteristica_acao' que vai importar os valores de 3 colunas diferentes baseadas no tipo de apoio técnico
    mask1 = (df_acoes['acao_realizada']=='Apoio Tecnico Presencial (ATP)')
    mask2 = (df_acoes['acao_realizada']=='Apoio Tecnico Não Presencial (ATNP)')
    mask3 = (df_acoes['acao_realizada']=='Outras Ações')
    list_mask = [mask1,mask2,mask3]
    list_col_use = ['1.Apoio Técnico Presencial (ATP)','2.Apoio Técnico Não Presencial (ATNP)','3.Outras Ações']
    for mask, col in zip(list_mask,list_col_use):
        df_acoes.loc[mask, 'caracteristica_acao'] = df_acoes[col]

    ### NOVA COLUNA 2 - Cria a coluna 'descricao_acao' que vai importar os valores de 3 colunas diferentes baseadas no tipo de apoio técnico
    mask1 = (df_acoes['acao_realizada']=='Apoio Tecnico Presencial (ATP)')
    mask2 = (df_acoes['acao_realizada']=='Apoio Tecnico Não Presencial (ATNP)')
    mask3 = (df_acoes['acao_realizada']=='Outras Ações')

    list_mask = [mask1,mask2,mask3]
    list_col_use = ['1.2 - Descrição da Ação (ATP)','2.2 - Descrição da Ação (ATNP)','3.2 - Descrição da Ação (Outras)']

    for mask, col in zip(list_mask,list_col_use):
        df_acoes.loc[mask, 'descricao_acao'] = df_acoes[col]
    
    ### NOVA COLUNA 3 - Cria a coluna 'n_profissionais_atendidos' que vai importar os valores de 3 colunas diferentes baseadas no tipo de apoio técnico
    mask1 = (df_acoes['acao_realizada']=='Apoio Tecnico Presencial (ATP)')
    mask2 = (df_acoes['acao_realizada']=='Apoio Tecnico Não Presencial (ATNP)')
    mask3 = (df_acoes['acao_realizada']=='Outras Ações')

    list_mask = [mask1,mask2,mask3]
    list_col_use = ['1.1 - Nº de profissionais atendidos(ATP)','2.1 - Nº de profissionais atendidos(ATNP)','3.1 - Nº de profissionais atendidos (Outras ações)']

    for mask, col in zip(list_mask,list_col_use):
        df_acoes.loc[mask, 'n_profissionais_atendidos'] = df_acoes[col]
        
    # cria coluna 'user_id' para ser usada no futuro
    # df_acoes['user_id'] = ''
    ## finaliza a base e armazena na variavel 'data'
    data = df_acoes[['nome_profissional','email','acao_realizada','caracteristica_acao','n_profissionais_atendidos','descricao_acao',
        'data_acao','data_publicacao','municipio_atendido']].copy()
        
    data.caracteristica_acao = data.caracteristica_acao.fillna('vazio')
    data.n_profissionais_atendidos   = data.n_profissionais_atendidos.fillna(0)
    
    return data
# importAcoes()