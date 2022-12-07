
from datetime import timezone
from secrets import choice
from django.db import models
from .choices_list import *
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    sector_name = models.CharField(max_length=100, choices=LISTA_SETORES)

    def __str__(self):
        return f'{self.sector_name}'

# # ### DATABASE DE AÇÕES
# class TableActionModel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabelaAcoes')
#     acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE)
#     caracteristica_acao = models.CharField(max_length=100, choices=TECNICO_PRESENCIAL_CHOICE, default= '')
#     caracteristica_acao = models.CharField(max_length=100, choices=TECNICO_NAO_PRESENCIAL_CHOICE, default='')
#     caracteristica_acao = models.CharField(max_length=100, choices=OUTRAS_ACOES_CHOICE, default= '(Não se aplica)')
#     n_profissionais_atendidos = models.IntegerField('Numero de Funcionario',blank=False, null=False)
#     descricao_acao = models.TextField('Descrição da Ação', max_length=1000, blank=False, null=False)
#     data_acao = models.DateField('Data', blank=False, null=False)
#     data_publicacao = models.DateField('Data da Publicação', default=timezone.now)
#     municipio_atendido = models.CharField(max_length=100, choices= LISTA_MUNICIPIOS, default= '(Não se aplica)')


#     def __str__(self):
#         return self.user.first_name

#####  ATENÇÃO: CRIAREMOS 3 TABELAS DIFERENTES PARA ATP/ATNP E OUTRAS AÇÕES.
#####... Unica todos os nomes de capos serão iguais, porem, o campo "caracteristica_acao" possui as "choices" diferentes,
#  baseado em cada tipo de ação realizada. isso tudo para poder concatenar com pandas depois, uma vez que todos os campos(nomes de coluna serão iguais)
# ### DATABASE DE AÇÕES - ATP
class AcaoAtpModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acaoAtp')
    acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE, default= 'Apoio Técnico Presencial (ATP)') # preenche automaticamente
    caracteristica_acao = models.CharField(max_length=100, choices=TECNICO_PRESENCIAL_CHOICE, default= '')
    n_profissionais_atendidos = models.IntegerField('Numero de Funcionario',blank=False, null=False)
    descricao_acao = models.TextField('Descrição da Ação', max_length=1000, blank=False, null=False)
    data_acao = models.DateField('Data', blank=False, null=False)
    data_publicacao = models.DateField('Data da Publicação', default=timezone.now)
    municipio_atendido = models.CharField(max_length=100, choices= LISTA_MUNICIPIOS, default= '')

    def __str__(self):
        return self.user.first_name

# ### DATABASE DE AÇÕES - ATNP
class AcaoAtnpModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acaoAtnp')
    acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE, default= 'Apoio Técnico Não Presencial (ATNP)')
    caracteristica_acao = models.CharField(max_length=100, choices=TECNICO_NAO_PRESENCIAL_CHOICE, default='')
    n_profissionais_atendidos = models.IntegerField('Numero de Funcionario',blank=False, null=False)
    descricao_acao = models.TextField('Descrição da Ação', max_length=1000, blank=False, null=False)
    data_acao = models.DateField('Data', blank=False, null=False)
    data_publicacao = models.DateField('Data da Publicação', default=timezone.now)
    municipio_atendido = models.CharField(max_length=100, choices= LISTA_MUNICIPIOS, default= '')

    def __str__(self):
        return self.user.first_name

# ### DATABASE DE AÇÕES - Outras ações
class AcaoOutrasModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='acaoOutras')
    acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE, default= 'Outras Ações')
    caracteristica_acao = models.CharField(max_length=100, choices=OUTRAS_ACOES_CHOICE, default= '')
    n_profissionais_atendidos = models.IntegerField('Numero de Funcionario',blank=False, null=False)
    descricao_acao = models.TextField('Descrição da Ação', max_length=1000, blank=False, null=False)
    data_acao = models.DateField('Data', blank=False, null=False)
    data_publicacao = models.DateField('Data da Publicação', default=timezone.now)
    municipio_atendido = models.CharField(max_length=100, choices= LISTA_MUNICIPIOS, default='')

    def __str__(self):
        return self.user.first_name








### TABELA DE EVENTOS
class TableEventModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tabelaEventos')
    titulo_evento = models.TextField('Titulo', max_length=150)
    tipo_evento = models.CharField(max_length=50, choices=TIPO_EVENTO_CHOICE, default='Híbrida')
    instituicao_ofertante = models.CharField('Instituição Ofertante', max_length=150,null=False, default='')
    data_inicial = models.DateField('Data Inicial')
    data_final = models.DateField('Data Final')
    descricao_evento = models.TextField('Descrição do Evento', max_length=1000,null=False, default='')
    data_publicacao = models.DateField('Data da Publicação', default=timezone.now)



### TABELA DE PARTICIPAÇÃO EM INSTANCIAS INTERSETORIAIS
class TableIntersetModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    espaco_participacao = models.CharField( max_length=150, choices=LISTA_ESPACO_PARTICIPACAO, default= '')
    data_inicial = models.DateField('Data Inicial')
    data_final = models.DateField('Data Final')
    descricao = models.TextField('Descrição', max_length=1000,null=False, default='')
    encaminhamentos = models.TextField('Encaminhamentos', max_length=1000,null=True, default='')


class ActionTypeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tipoAcoes')
    acao_realizada = models.CharField(max_length=100, choices= ACAO_REALIZADA_CHOICE, default= '')