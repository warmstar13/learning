from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from account.forms import TaskForm
from account.models import Account

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('account:login')
    else:
        form = UserCreationForm()
    context =  {'form': form}
    return render(request, 'account/register.html', context)


def mainpage(request):
    # get the information of current user with the same id
    if request.user.is_authenticated:
        user_instance = Account.objects.get(user_info=request.user)
        context = {'exp': user_instance.exp, 'username': user_instance.username}
        return render(request, 'account/mainpage.html', context)
    else:
        return render(request, 'account/mainpage.html')
    
def tasks(request):
    user_instance = Account.objects.get(user_info=request.user)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == '5':
            user_instance.exp += 5
            user_instance.save()
        elif action == '10':
            user_instance.exp += 10
            user_instance.save()
        elif action == '20':
            user_instance.exp += 20
            user_instance.save()
    context = {'exp': user_instance.exp}
    return render(request, 'account/tasks.html', context)

def leaderboard(request, page):
    if page < 1 or page > (Account.objects.count() + 9) // 10:
        return redirect('account:leaderboard', 1)
    start_top = (page - 1) * 10
    end_top = start_top + 10
    top_users = Account.objects.order_by('-exp')[start_top:end_top]
    first = page == 1
    last = page == (Account.objects.count() + 9) // 10
    context = {'top_users': top_users, 'page': page, 'first': first, 'last': last, 'start_top': start_top+1}
    return render(request, 'account/leaderboard.html', context)

def create_task(request):
    # what does taskform mean?
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.creator_account = Account.objects.get(user_info=request.user)
            task.save()
            return redirect('account:tasks')
    else:
        form = TaskForm()
    context = {'form': form}
    return render(request, 'account/create_task.html', context)
