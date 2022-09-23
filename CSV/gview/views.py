from gview.models import Person
import os
import pandas as pd

from django.views import View
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.
class UploadFile(View):
    def post(self, request, *args, **kwargs):
        context={}
        uploaded_file = request.FILES['document']
        if uploaded_file.name.endswith('.csv'):
                    #save the file in data folder
                d = os.path.join(os.getcwd(), 'data') 
                savefile = FileSystemStorage(d)
                file_directory = os.path.join(d, 'load.csv')
                if os.path.exists(file_directory):
                    os.remove(file_directory)
                savefile.save('load.csv', uploaded_file)
                    #know where to save the file
                #current directory of the project
                os.system('python3 manage.py runscript s_load')
        else:
            messages.warning(request, 'File was not uploaded. Please use csv file.')
            return render(request, 'main.html')
            
        return redirect('/table')



class MainView(View):
    template_name = None
    def get(self, request):
        return render(request, 'main.html')

class idListView(View):
    def get(self, request):
        data = Person.objects.all()
        return render(request, 'table.html', {'data': data})

class Alphabetically(View):
    def get(self, request):
        names = Person.objects.order_by('name')
        return render(request, 'alphabetical.html', {'names': names})

class Older(View):
    def get(self, request):
        ages = Person.objects.order_by('birthdate', 'name')
        return render(request, 'older.html', {'ages': ages})

class Younger(View):
    def get(self, request):
        edad = Person.objects.order_by('-birthdate', 'name')
        return render(request, 'younger.html', {'edad': edad})

class GenderType(View):
    def get(self, request):
        male_no = Person.objects.filter(gender='M').count()
        male_no = int(male_no)

        female_no = Person.objects.filter(gender='F').count()
        female_no = int(female_no)
        
        other_no = Person.objects.filter(gender='O').count()
        other_no = int(other_no)

        gender_list = ['Male', 'Female', 'Other']
        gender_number = [male_no, female_no, other_no]
        
        counting = {
            'gender_list': gender_list,
            'gender_number': gender_number,
        }
        return render(request, 'gendercount.html', counting)
    