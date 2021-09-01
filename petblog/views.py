from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})
# Create your views here.
# push video up to heroku for web hosting https://www.youtube.com/watch?v=UkokhawLKDU&list=PLCC34OHNcOtrZnQI6ZLvGPUWfQ6oh-D6H&index=13
# test git, turn on virt envirnment and then python manage.py runserver
