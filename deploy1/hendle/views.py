
# Create your views here.
import joblib
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import CreateUserForm,QuestionForm
'''from .filters import OrderFilter
'''
def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')


		context = {'form':form}
		return render(request, 'hendle/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'hendle/login.html', context)

# Create your views here.
def logoutUser(request):
	logout(request)
	return redirect('login')
def home(request):
	return render(request, 'hendle/dashboard.html')


def dash(request):
	return render(request, 'hendle/dashboard.html')

def question(request):
	ans="FILL ALL THE FIELDS CORRECTLY AND PRESS CHECK TO GET THE RESULTS"

	form=QuestionForm()
	if request.method=="POST":
		form=QuestionForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			print(type(form.cleaned_data))
			lis=[]
			for value in form.cleaned_data:
				if value=='name':
					continue
				if value=='Follicle_R' or value== 'Follicle_L' or value== 'Cycle':
					lis.append(float(form.cleaned_data[value]))
				else:
					if value=='Skin_darkening' or value=='hair_growth' or value=='Weight_gain':
						if form.cleaned_data[value]=='YES':
							lis.append(1)
						else:

							lis.append(0)
			print(lis)
			gnb=joblib.load('finalized_model1.sav')

			ans=gnb.predict([lis])
			print(ans)
	return render(request,'hendle/form.html',{'form':form,'ans':ans})
