from pickle import FALSE
from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from secrets import choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib import messages

from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import check_user_is_authenticated, user_required

import pandas as pd
import json
import plotly.graph_objects as go
import plotly.io as pio
import plotly.express as px
from datetime import datetime
from datetime import date


#### REGISTRO DE USURIOS ---------------------------------------------------------------------
@check_user_is_authenticated
def register_user(request):
    if request.method == 'POST':
        form = RegisterEmployee(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/users/contas/login/')
    else:
        form = RegisterEmployee()
    return render(request, 'app/register.html', {'form':form})

##### LOGIN / LOGOUT-----------------------------------------------------------------------------------------
@check_user_is_authenticated
def login_user(request):
    return render(request, 'app/registration/login.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/users/contas/login/")


#### REGISTRA NO FORMULARIO DE ACOES 
@user_required
class ACOES():
    ##1.PRESENTIAL ATP --------------------------
    def getAcaoAtp(request): # PRESENCIAL
        if request.method == 'POST':
            formAtp = AcaoAtpForm(request.POST)
            if formAtp.is_valid():
                profile = formAtp.save(commit=False)
                profile.user = request.user
                profile.save()
                formAtp.save()
                # print(request.POST.get('acao_realizada'))
                return redirect('/users/formulario-de-acao-atp')
        else:
            formAtp = AcaoAtpForm()
        return render(request, 'app/tables/tableAction/tableActionRegisterAtp.html', {'formAtp':formAtp})

    def deleteAtp(request, id): ### DELETE
        object_table_action = get_object_or_404(AcaoAtpModel, id=id)
        if request.method == "POST":
            object_table_action.delete()
            return redirect("/users/tabelas")
        return render(request, "delete_view.html")

    def updateAtp(request, id): ## UPDATE
        context = {}
        get_object_model = get_object_or_404(AcaoAtpModel, id=id)
        form = AcaoAtpForm(request.POST or None, instance=get_object_model)
        if form.is_valid():
            form.save()
            return redirect('/users/tabelas')
        context['form_table_action'] = form
        return render(request, "app/tables/tableAction/tableActionUpdate.html", context=context)
    
    def listAcaoAtp(request, id):
        acaoAtp_object_model = AcaoAtpModel.objects.filter(id=id)
        return render(request, 'app/tables/tableAction/listAcaoAtp.html',{
            'acaoAtp_object_model':acaoAtp_object_model})



    ##2.NAO PRESENCIAL ATNP -----------------------------
    def getAcaoAtnp(request): # NÃO PRESENCIAL
        if request.method == 'POST':
            formAtnp = AcaoAtnpForm(request.POST)
            if formAtnp.is_valid():
                profile = formAtnp.save(commit=False)
                profile.user = request.user
                profile.save()
                formAtnp.save()
                # print(request.POST.get('acao_realizada'))
                return redirect('/users/formulario-de-acao-atnp')
        else:
            formAtnp = AcaoAtnpForm()
        return render(request, 'app/tables/tableAction/tableActionRegisterAtnp.html', {'formAtnp':formAtnp})

    def deleteAtnp(request, id): ### DELETE
        object_table_action = get_object_or_404(AcaoAtnpModel, id=id)
        if request.method == "POST":
            object_table_action.delete()
            return redirect("/users/tabelas")
        return render(request, "delete_view.html")

    def updateAtnp(request, id): ## UPDATE
        context = {}
        get_object_model = get_object_or_404(AcaoAtnpModel, id=id)
        form = AcaoAtnpForm(request.POST or None, instance=get_object_model)
        if form.is_valid():
            form.save()
            return redirect('/users/tabelas')
        context['form_table_action'] = form
        return render(request, "app/tables/tableAction/tableActionUpdate.html", context=context)

    def listAcaoAtnp(request, id):
        acaoAtnp_object_model = AcaoAtnpModel.objects.filter(id=id)
        return render(request, 'app/tables/tableAction/listAcaoAtnp.html',{
            'acaoAtnp_object_model':acaoAtnp_object_model})

    ##3.OUTRAS ---------------------------
    def getAcaoOutras(request): # OUTRAS
        if request.method == 'POST':
            formOutras = AcaoOutrasForm(request.POST)
            if formOutras.is_valid():
                profile = formOutras.save(commit=False)
                profile.user = request.user
                profile.save()
                formOutras.save()
                # print(request.POST.get('acao_realizada'))
                return redirect('/users/formulario-de-acao-outras')
        else:
            formOutras = AcaoOutrasForm()
        return render(request, 'app/tables/tableAction/tableActionRegisterOutras.html', {'formOutras':formOutras})

    def deleteOutras(request, id): ### DELETE
        object_table_action = get_object_or_404(AcaoOutrasModel, id=id)
        if request.method == "POST":
            object_table_action.delete()
            return redirect("/users/tabelas")
        return render(request, "delete_view.html")
    
    def updateOutras(request, id): ## UPDATE
        context = {}
        get_object_model = get_object_or_404(AcaoOutrasModel, id=id)
        form = AcaoOutrasForm(request.POST or None, instance=get_object_model)
        if form.is_valid():
            form.save()
            return redirect('/users/tabelas')
        context['form_table_action'] = form
        return render(request, "app/tables/tableAction/tableActionUpdate.html", context=context)

    def listAcaoOutras(request, id):
        acaoOutras_object_model = AcaoOutrasModel.objects.filter(id=id)
        return render(request, 'app/tables/tableAction/listAcaoOutras.html',{
            'acaoOutras_object_model':acaoOutras_object_model})
    
    
    # def listAcao(request, id):
    #         df_atp = pd.DataFrame(list(AcaoAtpModel.objects.filter(user=request.user, id=id).values().order_by('-id')))
    #         df_atnp = pd.DataFrame(list(AcaoAtnpModel.objects.filter(user=request.user, id=id).values().order_by('-id')))
    #         df_outras = pd.DataFrame(list(AcaoOutrasModel.objects.filter(user=request.user, id=id).values().order_by('-id')))
    #         df = pd.concat([df_atp,df_atnp,df_outras])
    #         # df['data_acao'] = pd.to_datetime(df['data_acao']).dt.strftime('%d-%m-%y')
    #         json_records = df.reset_index().to_json(orient ='records')
    #         data_json_acoes = []
    #         data_json_acoes = json.loads(json_records)
    #         print(df)
    #         return render(request, 'app/tables/tableAction/listAcao.html', {'data_json_acoes':data_json_acoes,
    #                                                                 })



### REGISTRA O FORMULARIO DE EVENTOS -------------------------------------------------------------------------
# @login_required(login_url='contas/login')
@user_required
class EVENTO():
    def getEvento(request):
        if request.method == 'POST':
            formEvento = TableEventForm(request.POST)
            if formEvento.is_valid():
                profile = formEvento.save(commit=False)
                profile.user = request.user
                profile.save()
                return redirect('/users/formulario-de-eventos')
        else:
            formEvento = TableEventForm()
        return render(request, 'app/tables/tableEvent/tableEventRegister.html', {'formEvento':formEvento})

    def deleteEvento(request, id):
        object_table_event = get_object_or_404(TableEventModel, id=id)
        if request.method == "POST":
            object_table_event.delete()
            return redirect('/users/tabelas')
        return render(request, "delete_view.html")
    
    def updateEvento(request, id):
        context = {}
        get_object_model = get_object_or_404(TableEventModel, id=id)
        form = TableEventForm(request.POST or None, instance=get_object_model)

        if form.is_valid():
            form.save()
            return redirect('/users/tabelas')
        context = {'form_table_event':form}
        return render(request, 'app/tables/tableEvent/tableEventUpdate.html', context=context)
    
    def listEvento(request, id):
        evento_object_model = TableEventModel.objects.filter(id=id)
        return render(request, 'app/tables/tableEvent/listEvento.html',{'evento_object_model':evento_object_model})# context=context)


###---INSTANCIAS INTERSETORIAIS


@login_required(login_url='contas/login')
@user_required
class INTERSET():
    def getInterset(request):
        if request.method == 'POST':
            formInterset = TableIntersetForm(request.POST)
            if formInterset.is_valid():
                profile = formInterset.save(commit=False)
                profile.user = request.user
                profile.save()
                formInterset.save()
                return redirect('/users/formulario-de-intersetoriais')
        else:
            formInterset = TableIntersetForm()
        return render(request, 'app/tables/tableInterset/tableIntersetRegister.html', {'formInterset':formInterset})

    def deleteInterset(request, id):
        object_table_event = get_object_or_404(TableIntersetModel, id=id)
        if request.method == "POST":
            object_table_event.delete()
            return redirect('/users/tabelas')
        return render(request, "delete_view.html")
    
    def updateInterset(request, id):
        context = {}
        get_object_model = get_object_or_404(TableIntersetModel, id=id)
        form = TableIntersetForm(request.POST or None, instance=get_object_model)
        if form.is_valid():
            form.save()
            return redirect('/users/tabelas')
        context = {'formInterset':form}
        return render(request, 'app/tables/tableInterset/tableIntersetUpdate.html', context=context)
    
    def listInterset(request, id):
        interset_object_model = TableIntersetModel.objects.filter(id=id)
        return render(request, 'app/tables/tableInterset/listInterset.html',{'interset_object_model':interset_object_model})# context=context)

  
##### VISUALIZAR TABELAS ----------------------------------------------------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def tables(request):
    ###EX1: df = pd.DataFrame(list(AcaoOutrasModel.objects.all().values())) PEGA TODOS OS VALORES INDEPENDENTES DO USUARIO
    ###EX2:df = pd.DataFrame(list(AcaoAtnpModel.objects.filter(user=request.user).values().order_by('-id'))) PEGA OS VALORES BASEADOS NO USUARIO LOGADO

    ### usar pandas para concatenar as 3 tabalas em uma so. 
    df_atp = pd.DataFrame(list(AcaoAtpModel.objects.filter(user=request.user).values().order_by('-id')))
    df_atnp = pd.DataFrame(list(AcaoAtnpModel.objects.filter(user=request.user).values().order_by('-id')))
    df_outras = pd.DataFrame(list(AcaoOutrasModel.objects.filter(user=request.user).values().order_by('-id')))
    df = pd.concat([df_atp,df_atnp,df_outras])#.drop(columns=['user_id'])
    df['data_acao'] = pd.to_datetime(df['data_acao']).dt.strftime('%d-%m-%y')
    df = df.sort_values(by='data_acao', ascending=False)
    # print(df['data_acao'])
    # transformando dataframe em json para rodar com bootstrap
    json_records = df.reset_index().to_json(orient ='records')
    data_json_acoes = []
    data_json_acoes = json.loads(json_records)

    ### eventos dados
    page_object_evento = TableEventModel.objects.filter(user=request.user).values().order_by('-id')
    page_object_interset = TableIntersetModel.objects.filter(user=request.user).values().order_by('-id')



    # print(data_json)
    # context = {'d': data}
    return render(request, 'app/tables/viewAllTable.html', {'data_json_acoes':data_json_acoes,
                                                            'page_object_evento':page_object_evento,
                                                            'page_object_interset':page_object_interset,
                                                             })






def main(request):
    return render(request, 'app/main.html')


def dashboards(request):
    df_atp = pd.DataFrame(list(AcaoAtpModel.objects.filter(user=request.user).values().order_by('-id')))
    df_atnp = pd.DataFrame(list(AcaoAtnpModel.objects.filter(user=request.user).values().order_by('-id')))
    df_outras = pd.DataFrame(list(AcaoOutrasModel.objects.filter(user=request.user).values().order_by('-id')))
    df = pd.concat([df_atp,df_atnp,df_outras])#.drop(columns=['user_id'])
    df['data_acao'] = pd.to_datetime(df['data_acao'])#.dt.strftime('%d-%m-%y')
    df = df.sort_values(by='data_acao', ascending=False)

    t_atp = df.loc[df['acao_realizada']=='Apoio Técnico Presencial (ATP)'].shape[0]
    t_atnp = df.loc[df['acao_realizada']=='Apoio Técnico Não Presencial (ATNP)'].shape[0]
    t_outras = df.loc[df['acao_realizada']=='Outras Ações'].shape[0]
    t_acoes = df.shape[0]
    #GRAFICO 1
    fig1 = go.Figure(data=[go.Pie(labels=df.acao_realizada.value_counts().index, 
                              values=df.acao_realizada.value_counts().values, textinfo='percent',
                             hole=.3
                            )])
    fig1.update_layout(template=None, autosize=True, hovermode="x", title=None,
    margin=dict(l=20, r=20, t=20, b=20),
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.0,
                            xanchor="right",
                            x=1,
                            font=dict(size=12)))
    
    
    # GRAFICO 2
    dic_mes = {1:'Jan',2:'Fev',3:'Mar',4:'Abr',5:'Mai',6:'Jun',7:'Jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}
    df['n_mes_acao'] = df['data_acao'].dt.month
    df['mes_acao'] = df['n_mes_acao'].map(dic_mes)
    df['ano_acao'] = df['data_acao'].dt.year
    g2 = df.groupby(['n_mes_acao','mes_acao','data_acao','acao_realizada']).id.count().unstack().reset_index().rename_axis(None,axis=1).fillna(0).copy()
    g2 = g2.groupby(['n_mes_acao','mes_acao']).sum().reset_index()

    fig2 = go.Figure()
    if 'Apoio Técnico Presencial (ATP)' in g2.columns:
        fig2.add_trace(go.Bar(x=g2.mes_acao,  # index por que? porque o index é a 'date'
                                y=g2['Apoio Técnico Presencial (ATP)'],
                                marker_color='#F4D03F',
                                name='ATP',
                                hovertemplate='%{y:,.0f}'
                                ))
    if 'Apoio Técnico Não Presencial (ATNP)' in g2.columns:
        fig2.add_trace(go.Bar(x=g2.mes_acao,
                                    y=g2['Apoio Técnico Não Presencial (ATNP)'],
                                    marker_color='#A569BD',
                                    name='ATNP',
                                    hovertemplate='%{y:,.0f}'))
    if 'Outras Ações' in g2.columns:
        fig2.add_trace(go.Bar(x=g2.mes_acao,
                                    y=g2['Outras Ações'],
                                    marker_color='#CACFD2',
                                    name='OUTRAS',
                                    hovertemplate='%{y:,.0f}'))

    fig2.update_layout(template=None, autosize=True, hovermode="x", title=None,
    margin=dict(l=20, r=20, t=20, b=20),
                        legend=dict(
                            orientation="h",
                            yanchor="bottom",
                            y=1.0,
                            xanchor="right",
                            x=1,
                            font=dict(size=12)))
    
    
    ### GERAR TABELAS DE CARACTERISTICAS DAS ACOES
    #TAB1 = ATNP
    tab1 = df.loc[df['acao_realizada']=='Apoio Técnico Não Presencial (ATNP)'].groupby(['caracteristica_acao','n_mes_acao']).size().unstack().reset_index().rename_axis(None,axis=1).fillna(0)
    dic_group_mes = {'caracteristica_acao':'Apoio Técnico Não Presencial (ATNP)',1:'Jan',2:'Fev',3:'Mar',4:'Abr',5:'Mai',6:'Jun',7:'Jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}
    tab1.columns = tab1.columns.map(dic_group_mes)
    tab1.iloc[:,1:] = tab1.iloc[:,1:].astype(int)
    #TAB2 = ATP
    tab2 = df.loc[df['acao_realizada']=='Apoio Técnico Presencial (ATP)'].groupby(['caracteristica_acao','n_mes_acao']).size().unstack().reset_index().rename_axis(None,axis=1).fillna(0)
    dic_group_mes = {'caracteristica_acao':'Apoio Técnico Presencial (ATP)',1:'Jan',2:'Fev',3:'Mar',4:'Abr',5:'Mai',6:'Jun',7:'Jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}
    tab2.columns = tab2.columns.map(dic_group_mes)
    tab2.iloc[:,1:] = tab2.iloc[:,1:].astype(int)
    #TAB3 = Outras Ações
    tab3 = df.loc[df['acao_realizada']=='Outras Ações'].groupby(['caracteristica_acao','n_mes_acao']).size().unstack().reset_index().rename_axis(None,axis=1).fillna(0)
    dic_group_mes = {'caracteristica_acao':'Outras Ações',1:'Jan',2:'Fev',3:'Mar',4:'Abr',5:'Mai',6:'Jun',7:'Jul',8:'Ago',9:'Set',10:'Out',11:'Nov',12:'Dez'}
    tab3.columns = tab3.columns.map(dic_group_mes)
    tab3.iloc[:,1:] = tab3.iloc[:,1:].astype(int)
    
    tab1_json = tab1.reset_index().to_json(orient ='records')
    tab1_json = json.loads(tab1_json)

    df['data_acao'] = pd.to_datetime(df['data_acao']).dt.strftime('%d-%m-%y')
    # transformando dataframe em json para rodar com bootstrap
    json_records = df.reset_index().to_json(orient ='records')
    data_json_acoes = []
    data_json_acoes = json.loads(json_records)

    # print(data_json)
    # context = {'d': data}
    return render(request, 'app/dashboards/painelAcoes.html', {
        'tab1_col':tab1.columns,
        'tab1_row':tab1.values,
        'tab2_col':tab2.columns,
        'tab2_row':tab2.values,
        'tab3_col':tab3.columns,
        'tab3_row':tab3.values,
        't_atp':t_atp,
        't_atnp':t_atnp,
        't_outras':t_outras,
        't_acoes':t_acoes,
        'data_json_acoes':data_json_acoes,
        'fig1':fig1.to_html(),
        'fig2':fig2.to_html(),
         })



# def tables(request):
#     return render(request, 'app/tables.html')


# def register(request):
#     return render(request, 'app/register.html')


# def login(request):
#     return render(request, 'app/login.html')


def charts(request):
    return render(request, 'app/charts.html')


def password(request):
    return render(request, 'app/password.html')


