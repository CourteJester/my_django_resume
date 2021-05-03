from django.shortcuts import render 
import datetime

 #Create your views here.
def home(request):
	return render(request, 'home.html', {})
	
#def home1(request):
#	from resume.name_file import names_function
#	names = ["Eric", "Stan", "Kyle", "Kenny"]
#	return render(request, 'home1.html', {'names': names, 'namer' : names_function})

#def about(request):
#	f_name = "Gargamel"
#	l_name = "Smith"
#	t_date = datetime.datetime.now()
#	return render(request, 'about-me.html', {'first_name': f_name, 'last_name': l_name, 'today_date': t_date })

