from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class QuestionForm(forms.Form):
	name=forms.CharField()
	Follicle_R=forms.DecimalField( max_digits=20,  decimal_places=10)
	Follicle_L=forms.DecimalField( max_digits=20,  decimal_places=10)
	Skin_darkening=forms.ChoiceField(choices=[('YES','YES'),('NO','NO')])
	hair_growth=forms.ChoiceField(choices=[('YES','YES'),('NO','NO')])
	Weight_gain=forms.ChoiceField(choices=[('YES','YES'),('NO','NO')])
	Cycle=forms.DecimalField( max_digits=20,  decimal_places=10)
