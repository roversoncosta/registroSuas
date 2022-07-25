from dataclasses import fields
from pickle import LIST
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput, ModelForm

from app.models import *
from .choices_list import LISTA_SETORES



### FORMULARIO D EREGISTRO DE USUÁRIO/PROFISSIONAIS
class RegisterEmployee(UserCreationForm):
    username = forms.CharField(help_text="Necessário ter um Usuario para ser seu login", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um usuario para acessar sua conta'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Primeiro Nome'}), max_length=32, help_text='Digite o seu Primeiro nome')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}), max_length=32, help_text='Sobrenome')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Entre com um Endereço Válido')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha novamente'}))
    sector_name = forms.ChoiceField(
        choices=LISTA_SETORES,  
    )
    #Usando o Models User do 'relatorios/models'
    class Meta(UserCreationForm):
        model = User
        fields = UserCreationForm.Meta.fields + ('sector_name','first_name', 'last_name', 'email',)
    
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.sector_name = self.cleaned_data['sector_name']
        user.set_password(self.cleaned_data['password1'])

        if User.objects.filter(email=user.email).exists():
            raise forms.ValidationError('Email já cadastrado')
        elif User.objects.filter(username=user.username).exists():
            raise forms.ValidationError('Este usuário já existe')
        else:
            if commit:
                user.save()

    def __init__(self, *args, **kwargs):
        super(RegisterEmployee, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control my-1'

### FORMULARIO DE AÇÕES
class TableActionForm(ModelForm):
    class Meta:
        model = TableActionModel
        fields = ['acao_realizada', 'tecnico_presencial', 'tecnico_nao_presencial',
        'outras_acoes', 'n_profissionais_atendidos', 'descricao_acao', 'data_acao','municipio_atendido']
        labels = {
                    "acao_realizada": "TIPO DA AÇÃO:",
                    "tecnico_presencial": "Apoio Técnico Presencial:",
                    "tecnico_nao_presencial": "Apoio Técnico Não Presencial:",
                    "outras_acoes": "Outras Ações:",
                    "n_profissionais_atendidos": "Nº de Profissionais atendidos:",
                    "descricao_acao":"Descreva brevemente o tipo de demanda atendida:",
                    "data_acao":"Data da ação realizada:",
                    "municipio_atendido":"Município Atendido"

                    }

        widgets = {
            'data_acao': forms.DateInput(attrs={'type':'date'}),
        }
    # def __init__(self, *args, **kwargs):
    #     super(TableActionForm, self).__init__(*args, **kwargs)
    #     self.fields['n_profissionais_atendidos'].label = "Numero de Funcionarios Atendidos"

#### FORMULARIO DE EVENTOS
class TableEventForm(ModelForm):
    class Meta:
        model = TableEventModel
        fields = ['titulo_evento', 'tipo_evento', 'instituicao_ofertante','data_inicial', 'data_final','descricao_evento']
        labels = {
            'titulo_evento':"Título do evento", 
            'tipo_evento':"Tipo de evento", 
            'instituicao_ofertante':"Intituição ofertante",
            'data_inicial':"Data inicial", 
            'data_final':"Data final",
            'descricao_evento':"Descrição do Evento"
            }
        widgets = {
            'titulo_evento': forms.TextInput(),
            'data_inicial': forms.DateInput(attrs={'type':'date'}),
            'data_final': forms.DateInput(attrs={'type':'date'})
        }

    def clean(self):
        super(TableEventForm, self).clean()

        titulo_evento = self.cleaned_data.get("title_event")
        tipo_evento = self.cleaned_data.get("event_feature")
        data_inicial = self.cleaned_data.get("date_initial")
        data_final = self.cleaned_data.get("date_final")

        return self.cleaned_data


    # def __init__(self, *args, **kwargs):
    #     super(TableEventForm, self).__init__(*args, **kwargs)
    #     self.fields['tipo_evento'].label = "Característica do Evento"


### FORMULARIO DE REGISTRO DE PARTICIPAÇÃO EM INSTANCIAS INTERSETORIAIS DO SUAS
class TableIntersetForm(ModelForm):
    class Meta:
        model = TableIntersetModel
        fields = ['espaco_participacao','data_inicial','data_final','descricao','encaminhamentos']
        labels ={
            'espaco_participacao':'Espaço de participação',
            'data_inicial':'Data inicial',
            'data_final':'Data final',
            'descricao':'Descrição',
            'encaminhamentos':'Encaminhamentos (caso houve algum)'
        }   
        widgets = {
            'data_inicial': forms.DateInput(attrs={'type':'date'}),
            'data_final': forms.DateInput(attrs={'type':'date'})
        }     


