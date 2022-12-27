import pandas as pd
def importInterset():
    link_registros ='https://docs.google.com/spreadsheets/d/e/2PACX-1vSSSzbKEW5XI8PKTj9mueR1cGi_GlTeUOmWVYIm9-i-zbCoZpelscZv_YSj4MXVcf4kN-_VY0AFpNDm/pub?gid=1021085548&single=true&output=csv'
    reg = pd.read_csv(link_registros)
    df_inter = reg.loc[reg['REGISTRAR:']=='PARTICIPAÇÃO EM INSTÂNCIAS DO SUAS E INTERSETORIAIS']\
    [['DATA DA PARTICIPAÇÃO', 'LOCAL', 'DESCRIÇÃO', 'ENCAMINHAMENTOS',
        'ESPAÇO DE PARTICIPAÇÃO - INSTÂNCIAS DO SUAS',
        'ESPAÇO DE PARTICIPAÇÃO - INSTÂNCIAS INTERSETORIAIS','email']]

    # ### renomeia algumas colunas
    data = df_inter.rename(columns=
    {
    'DATA DA PARTICIPAÇÃO':'data_participacao',
    'LOCAL':'local',
    'DESCRIÇÃO':'descricao',
    'ENCAMINHAMENTOS':'encaminhamentos',
    'ESPAÇO DE PARTICIPAÇÃO - INSTÂNCIAS DO SUAS':'espaco_participacao_suas',
    'ESPAÇO DE PARTICIPAÇÃO - INSTÂNCIAS INTERSETORIAIS':'espaco_participacao_intersetoriais',
    'email':'email'
    })
        
    return data


    