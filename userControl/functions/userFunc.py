from django.contrib.auth import authenticate, login
from ..forms import LoginForm, UserRegistrationForm


def addNewUser(request, error=False):
	user_form = UserRegistrationForm(request.POST)
	print(user_form.errors)
	if user_form.is_valid():
		new_user = user_form.save(commit=False)
		new_user.set_password(user_form.cleaned_data['password'])
		new_user.save()
	else:
		error = 'Ошибка в форме!'
	return error


def authorize(request, error=True):
	form = LoginForm(request.POST)
	print(form.errors)
	if form.is_valid():
		cd = form.cleaned_data
		user = authenticate(username=cd['username'], password=cd['password'])
		if user is not None:
			if user.is_active:
				login(request, user)
				error = False
			else:
				error = 'Disabled account'
		else:
			error = 'Invalid login'
	return error