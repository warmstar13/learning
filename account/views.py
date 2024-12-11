from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from account.models import Account

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context =  {'form': form}
    return render(request, 'account/register.html', context)

@login_required
def mainpage(request):
    # get the information of current user with the same id
    user_instance = Account.objects.get(user_info=request.user)
    context = {'exp': user_instance.exp, 'username': user_instance.username}
    return render(request, 'account/mainpage.html', context)
