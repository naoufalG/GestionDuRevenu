from pyexpat.errors import messages

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from Accounts.forms import UserForm

# Create your views here.

def index(request):
    return render(request, "index.html")





def signup(request):
    if request.user.is_authenticated:
        return redirect('profile', username=request.user.username)

    if request.method == 'POST':
        f = UserForm(request.POST)
        if f.is_valid():
            f.save()
            return redirect('login')

    else:
        f = UserForm()

    return render(request, "registration/signup.html", {'form': f})
