> **15 Dezembro 2022**

**1. Transferir dados do Drive do RU para o banco de dados do projeto.**
- **Desafio 1**: Alguns registros de data na coluna ```data_acao``` no drive estavam com o ano digitado de forma errada (ex: *30/06/220*). O arquivo populate.py encontrava erro de formato de data nesta coluna.
- **Solucao**: Alterada manualmente na planilha de respostas no Drive essas datas com erros.

**Desafio 2:** Ao rodar o arquivo populate.py agora ele tranferiu os dados mas os botoes do CRUS nao estao funcionando para este registros.

PROXIMAS TAREFAS:
    importar DADOS E DF_USERS; FAZER MERGE PARA PASSASR OS ID DE USUARIO PARA A TABELA DADOS A SEREM REALIZADOS O BULKCREATE.
    Isso tdo no arquivo populate.py, funcao test_data()
    OBS: ultimo teste nao deu certo. acho que precisa excluir os usuarios criados manualmente e deixar apenas os usuarios criados no bulk_create (da base de dados dos registro no drive)