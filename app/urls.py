from atexit import register
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('registrar', view=register_user, name="register_user"),
    # path('formulario-de-evento', view=table_event, name='table_event'),
    # path('formulario-de-acao', view=table_action, name="table_action"),
    # path('formulario-de-instancias', view=table_interset, name="table_interset"),
    # path('tabelas', view=tables, name="tables"),
    # path('tabelas/<id>', view=description_table, name="description_table"),
    # path('deleteTableAction/<id>', view=deleteTableAction, name="deleteTableAction"),
    # path('deleteTableIntersetorial/<id>', view=deleteTableInterset, name="deleteTableInterset"),
    # path('deleteTableEvent/<id>', view=deleteTableEvent, name="deleteTableEvent"),
    # path('atualizar-tabela-acao/<id>', view=table_action_update, name="tableActionUpdate"),
    # path('atualizar-tabela-intersetorial/<id>', view=table_interset_update, name="tableIntersetUpdate"),
    # path('atualizar-tabela-eventos/<id>', view=table_event_update, name="tableEventUpdate"),
    # path('test/', view=testPath, name="testPath")
]
