import pandas as pd
def importEventos():
    link_registros ='https://docs.google.com/spreadsheets/d/e/2PACX-1vSSSzbKEW5XI8PKTj9mueR1cGi_GlTeUOmWVYIm9-i-zbCoZpelscZv_YSj4MXVcf4kN-_VY0AFpNDm/pub?gid=1021085548&single=true&output=csv'
    reg = pd.read_csv(link_registros)
    reg  = reg.loc[reg['REGISTRAR:']=='EVENTOS DE FORMAÇÃO DA EQUIPE TÉCNICA ESTADUAL']\
        [['Data de início','Data de término','Título do Evento','Instituição Ofertante','Característica do Evento','Nome do Profissional','Setor que atua',	'Descrição do evento','email']]

    data = reg.rename(columns={
        'Data de início':'data_inicial', 
        'Data de término':'data_final', 
        'Título do Evento':'titulo_evento',
        'Instituição Ofertante':'instituicao_ofertante', 
        'Característica do Evento':'tipo_evento',
        'Nome do Profissional':'nome_profissional', 
        'Setor que atua':'setor', 
        'Descrição do evento':'descricao_evento',
        'email':'email'
    })    
    
    return data


    