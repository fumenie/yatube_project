from django.http import HttpResponse
# from django.http import render

# Create your views here.


def index(request):
    return HttpResponse('Главная страница*-*')


def group_posts(request, slug):
    return HttpResponse(f'Выберите интересующую Вас тему. Например, {slug}')
