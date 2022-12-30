from atexit import register
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import * 

# ACOES = ACOES.getAcaoAtp()

urlpatterns = [
    # REGISTRAR USUARIOS
    path('registrar', view=register_user, name="register_user"),

    path('painel-acoes', view=dashboards, name="dashboards"),

    ### ACOES -------------------------->>>>>>>>>
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
    #LISTAR ACOES
    path('list-acao-atp/<id>', view =ACOES.listAcaoAtp,name="listAcaoAtp"),
    path('list-acao-atnp/<id>', view =ACOES.listAcaoAtnp,name="listAcaoAtnp"),
    path('list-acao-outras/<id>', view =ACOES.listAcaoOutras,name="listAcaoOutras"),
    
    ### EVENTOS -------------------------->>>>>>>>>
    #CRIAR EVENTOS
    path('formulario-de-eventos', view=EVENTO.getEvento, name="getEvento"),   
    #DELETAR EVENTOS
    path('deletar-tabela-evento/<id>', view=EVENTO.deleteEvento, name="deleteEvento"),
    #ATUALIZAR EVENTOS
    path('atualizar-tabela-evento/<id>', view=EVENTO.updateEvento, name="updateEvento"),
    #LISTAR EVENTOS
    path('list-evento/<id>', view = EVENTO.listEvento,name="listEvento"),

    ### INTERSETPRIAIS SUAS -------------------------->>>>>>>>>
    #CRIAR INTERSETORIAIS
    path('formulario-de-intersetoriais', view=INTERSET.getInterset, name="getInterset"),
    #DELETAR INTERSETORIAIS
    path('deletar-tabela-intersetoriais/<id>', view=INTERSET.deleteInterset, name="deleteInterset"),
    #ATUALIZAR INTERSETORIAIS
    path('atualizar-tabela-intersetoriais/<id>', view=INTERSET.updateInterset, name="updateInterset"),
    #LISTAR INTERSETORIAIS
    path('list-interset/<id>', view = INTERSET.listInterset,name="listInterset"),
    
    # VER TABELAS
    path('tabelas', view=tables, name="tables"),
    

    
]
