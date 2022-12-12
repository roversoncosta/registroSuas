from atexit import register
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import * 

# ACOES = ACOES.getAcaoAtp()

urlpatterns = [
    # REGISTRAR USUARIOS
    path('registrar', view=register_user, name="register_user"),

    #CRIAR ACOES
    path('formulario-de-acao-atp', view=ACOES.getAcaoAtp, name="getAcaoAtp"),
    path('formulario-de-acao-atnp', view=ACOES.getAcaoAtnp, name="getAcaoAtnp"),
    path('formulario-de-acao-outras', view=ACOES.getAcaoOutras, name="getAcaoOutras"),
    #DELETAR AÇÕES
    path('deletar-tabela-acao-atp/<id>', view=ACOES.deleteAtp, name="deleteAtp"),
    path('deletar-tabela-acao-atnp/<id>', view=ACOES.deleteAtnp, name="deleteAtnp"),
    path('deletar-tabela-acao-outras/<id>', view=ACOES.deleteOutras, name="deleteOutras"), 
    #ATUALIZAR ACOES
    path('atualizar-tabela-acao-atp/<id>', view=ACOES.updateAtp, name="updateAtp"),
    path('atualizar-tabela-acao-atnp/<id>', view=ACOES.updateAtnp, name="updateAtnp"),
    path('atualizar-tabela-acao-outras/<id>', view=ACOES.updateOutras, name="updateOutras"),
    
    #CRIAR EVENTOS
    path('formulario-de-evento/', view=EVENTO.getEvento, name="getEvento"),   
    #DELETAR EVENTOS
    path('deletar-tabela-evento/<id>', view=EVENTO.deleteEvento, name="deleteEvento"),
    #ATUALIZAR EVENTOS
    path('atualizar-tabela-evento/<id>', view=EVENTO.updateEvento, name="updateEvento"),
    
    #CRIAR INTERSETORIAIS
    path('formulario-de-intersetoriais', view=INTERSET.getInterset, name="getInterset"),
    #DELETAR INTERSETORIAIS
    path('deletar-tabela-intersetoriais/<id>', view=INTERSET.deleteInterset, name="deleteInterset"),
    #ATUALIZAR INTERSETORIAIS
    path('atualizar-tabela-intersetoriais/<id>', view=INTERSET.updateInterset, name="updateInterset"),
    
    
    # VER TABELAS
    path('tabelas', view=tables, name="tables"),
    # DETALHAR
    path('list-acao/<id>', view = ACOES.listAcaoAtp,name="listAcao"),

    path('list-acao-atp/<id>', view =ACOES.listAcaoAtp,name="listAcaoAtp"),
    path('list-acao-atnp/<id>', view =ACOES.listAcaoAtnp,name="listAcaoAtnp"),
    path('list-acao-outras/<id>', view =ACOES.listAcaoOutras,name="listAcaoOutras"),
    path('list-evento/<id>', view = EVENTO.listEvento,name="listEvento"),
    path('list-interset/<id>', view = INTERSET.listInterset,name="listInterset"),
    
    # path('tabelas-detalhes/<id>',view=ACOES.tablesDetails, name='tablesDetails'),

    # path('principal-usuario', view=index_users, name="index_users"),
    # path('formulario-de-evento', view=getEvento, name='getEvento'),
    # path('formulario-de-acao', view=table_action, name="table_action"),
    # path('formulario-de-instancias', view=getInterset, name="getInterset"),
 
    # path('tabelas/<id>', view=description_table, name="description_table"),
    # path('deleteTableAction/<id>', view=ACOES.deleteTableAction, name="deleteTableAction"),
    # path('atualizar-tabela-acao/<id>', view=ACOES.table_action_update, name="tableActionUpdate"),
    # path('deleteTableIntersetorial/<id>', view=deleteInterset, name="deleteInterset"),
    # path('deleteTableEvent/<id>', view=deleteTableEvent, name="deleteTableEvent"),

    # path('atualizar-tabela-intersetorial/<id>', view=updateInterset, name="tableIntersetUpdate"),
    # path('atualizar-tabela-eventos/<id>', view=table_event_update, name="tableEventUpdate"),
    
    
]
