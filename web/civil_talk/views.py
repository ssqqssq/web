from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.contrib.auth.decorators import login_required


def home(request):
    data = {'values': ['start', 'hello', 'shop']}
    return render(request, 'civil_talk/1home.html', data)


@login_required
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user  # Присвоение владельца статье
            article.save()
            return redirect('circulation_status')
        else:
            error = 'Форма была не верной'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'civil_talk/2circulation.html', data)


@login_required
def circulation_status(request):
    human_circulations = Articles.objects.filter(owner=request.user).order_by('date')
    context = {'articles': human_circulations}
    return render(request, 'civil_talk/3circulation_status.html', context)


def about(request):
    return render(request, 'civil_talk/4about.html')


