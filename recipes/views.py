from django.shortcuts import render


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Pedro Lucas',
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe-views.html', context={
        'name': 'Pedro Lucas',
    })
