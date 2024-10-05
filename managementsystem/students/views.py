from django.http  import JsonResponse
from django.views import View
from django.shortcuts import get_list_or_404 #importando um erro caso não retorne um objeto do banco de dados.
from models import Students
import json

#Isentar verificações de segurança
from django.views.decoratores.csrf import csrf_exempt
from django.utils.decoratores import method_decorator

# Create your views here.

class StudentListView(View):
  pass

class StudentCreateView(View):
  pass

class StudentCreateView(View):
  pass

class StundetDetailView(View):
  pass
