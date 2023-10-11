from django.shortcuts import render

# Create your views here.

from django.http.response import HttpResponse

from bugs.forms import registerbugs
from bugs.models import Bugs
from .models import Bugs

import django_tables2 as tables 


def index(request):
    return HttpResponse("Hello, world. You're at the bugs index.")


def contact_page_view(request):
    return HttpResponse("This is the contact page")

def register(request):
	context = {}

	# create object of form
	form = registerbugs(request.POST or None, request.FILES or None)
	
	# check if form data is valid
	if form.is_valid():
		# save the form data to model
		form.save()

	context['form']= form
	return render(request, "bugs/register.html", context)


# def display(request):
   # data = Bugs.objects.all()
    #return render(request,'bugs/index.html',{'datas': data })

# def info(request,data_id):
    #datar = Bugs.objects.get(pk = data_id)
   # datar = Bugs._meta.get_fields(data_id) 
    
    #return render(request,'bugs/info.html',{'datarrr': datar })

# this class will create the table just like how we create forms
class SimpleTable(tables.Table):
   class Meta:
      model = Bugs

# this will render table
class TableView(tables.SingleTableView):
   table_class = SimpleTable
   queryset = Bugs.objects.all()
   template_name = "table_example.html"