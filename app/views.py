from django.shortcuts import render


# Create your views here.
from secrets import choice
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login,  logout
from django.contrib import messages

from app.models import User
from .forms import *
from django.contrib.auth.decorators import login_required
from .decorators import check_user_is_authenticated, user_required



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
def login_user(request):
    return render(request, 'app/registration/login.html')

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/users/contas/login/")


#### REGISTRA O FORMULARIO DE EVENTOS -------------------------------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def table_event(request):
    if request.method == 'POST':
        form_table_event = TableEventForm(request.POST)
        if form_table_event.is_valid():
            profile = form_table_event.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/users/formulario-de-evento')
    else:
        form_table_event = TableEventForm()
    return render(request, 'app/tables/tableEvent/tableEventRegister.html', {'form_table_event':form_table_event})


#### REGISTRA O FORMULARIO DE ACOES -------------------------------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def table_action(request):
    if request.method == 'POST':
        form_table_action = TableActionForm(request.POST)
        if form_table_action.is_valid():
            profile = form_table_action.save(commit=False)
            profile.user = request.user
            profile.save()
            form_table_action.save()
            # print(request.POST.get('acao_realizada'))
            return redirect('/users/formulario-de-acao')
    else:
        form_table_action = TableActionForm()
    return render(request, 'app/tables/tableAction/tableActionRegister.html', {'form_table_action':form_table_action})


#### TESTANDO TIPO DE AÇÕES S -------------------------------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def action_type(request):
    if request.method == 'POST':
        form_action_type = ActionTypeForm(request.POST)
        if form_action_type.is_valid():
            profile = form_action_type.save(commit=False)
            profile.user = request.user
            profile.save()
            form_action_type.save()
            
            choice_action = request.POST.get('acao_realizada')
            #Se tipo foi ATP:
            form_table_action = TableActionForm()
            form_table_action['acao_realizada'] = choice_action
            if choice_action == 'Apoio Técnico Presencial (ATP)':
                return render(request, 'app/tables/tableAction/tableActionRegisterATP.html', {'form_table_action':form_table_action})
            
    else:
        form_action_type = TableActionForm()
    return render(request, 'app/tables/tableAction/tableActionRegister.html', {'form_table_action':form_action_type})





#### REGISTRA O FORMULARIO DE PATICIPAÇÃO EM INSTANCIAS DO SUAS----------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def table_interset(request):
    if request.method == 'POST':
        form_table_interset = TableIntersetForm(request.POST)
        if form_table_interset.is_valid():
            profile = form_table_interset.save(commit=False)
            profile.user = request.user
            profile.save()
            form_table_interset.save()
            return redirect('/users/forlulario-de-instancias')
    else:
        form_table_interset = TableIntersetForm()
    return render(request, 'app/tables/tableInterset/tableIntersetRegister.html', {'form_table_interset':form_table_interset})

# DELETAR 
@login_required(login_url='contas/login')
@user_required
def deleteTableInterset(request, id):
    object_table_interset = get_object_or_404(TableIntersetModel, id=id)
    if request.method == "POST":
        object_table_interset.delete()
        return redirect('/users/tabelas')
    return render(request, "delete_view.html")

# ATUALIZAR
@login_required(login_url='contas/login')
@user_required
def table_interset_update(request, id):
    context = {}
    get_object_model = get_object_or_404(TableIntersetModel, id=id)
    form = TableIntersetForm(request.POST or None, instance=get_object_model)
    if form.is_valid():
        form.save()
        return redirect('/users/tabelas')
    context = {'form_table_interset':form}
    return render(request, 'tables/tableInterset/tableIntersetUpdate.html', context=context)








##### VISUALIZAR TABELAS ----------------------------------------------------------------------------------------------
@login_required(login_url='contas/login')
@user_required
def tables(request):
    table_action_page_object = TableActionModel.objects.filter(user=request.user).values().order_by('-id')
    table_event_page_object = TableEventModel.objects.filter(user=request.user).values().order_by('-id')
    table_interset_page_object = TableIntersetModel.objects.filter(user=request.user).values().order_by('-id')

    return render(request, 'app/tables/viewAllTable.html',
    {
    'table_action_page_object':table_action_page_object,
    'table_event_page_object':table_event_page_object,
    'table_interset_page_object':table_interset_page_object,
    
    })



#Descrição das Tabelas
@login_required(login_url='contas/login')
@user_required
def description_table(request, id):
    table_action_page_object = TableActionModel.objects.filter(user=request.user).values().order_by('-id')
    table_event_page_object = TableEventModel.objects.filter(user=request.user).values().order_by('-id')
    id_description = get_object_or_404(table_action_page_object, id=id)

    return render(request, 'tables/tableAction/tableActionGetDescription.html', 
    {'id_description':id_description,
    'table_action_page_object':table_action_page_object,
    'table_event_page_object':table_event_page_object})



#deletar tabelas
@login_required(login_url='contas/login')
@user_required
def deleteTableAction(request, id):
    object_table_action = get_object_or_404(TableActionModel, id=id)

    if request.method == "POST":
        object_table_action.delete()
        return redirect("/users/tabelas")
    return render(request, "delete_view.html")

@login_required(login_url='contas/login')
@user_required
def deleteTableEvent(request, id):
    object_table_event = get_object_or_404(TableEventModel, id=id)
    if request.method == "POST":
        object_table_event.delete()
        return redirect('/users/tabelas')
    return render(request, "delete_view.html")


@login_required(login_url='contas/login')
@user_required
def table_action_update(request, id):
    context = {}

    get_object_model = get_object_or_404(TableActionModel, id=id)
    form = TableActionForm(request.POST or None, instance=get_object_model)

    if form.is_valid():
        form.save()
        return redirect('/users/tabelas')
    context['form_table_action'] = form
    return render(request, "tables/tableAction/tableActionUpdate.html", context=context)

@login_required(login_url='contas/login')
@user_required
def table_event_update(request, id):
    context = {}
    get_object_model = get_object_or_404(TableEventModel, id=id)
    form = TableEventForm(request.POST or None, instance=get_object_model)

    if form.is_valid():
        form.save()
        return redirect('/users/tabelas')
    context = {'form_table_event':form}
    return render(request, 'tables/tableEvent/tableEventUpdate.html', context=context)




def index_users(request):
    return render(request, 'app/index_users.html')


def index(request):
    return render(request, 'app/index.html')


# def tables(request):
#     return render(request, 'app/tables.html')


def register(request):
    return render(request, 'app/register.html')


def login(request):
    return render(request, 'app/login.html')


def charts(request):
    return render(request, 'app/charts.html')


def password(request):
    return render(request, 'app/password.html')
