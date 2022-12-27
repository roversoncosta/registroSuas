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


def index(request):
    return render(request, 'app/index.html')


# def tables(request):
#     return render(request, 'app/tables.html')


# def register(request):
#     return render(request, 'app/register.html')


def login(request):
    return render(request, 'app/login.html')


def charts(request):
    return render(request, 'app/charts.html')


def password(request):
    return render(request, 'app/password.html')


