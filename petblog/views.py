from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# Create your views here.
# push video up to heroku for web hosting https://www.youtube.com/watch?v=UkokhawLKDU&list=PLCC34OHNcOtrZnQI6ZLvGPUWfQ6oh-D6H&index=13
# test git, turn on virt envirnment and then python manage.py runserver

#from .forms import PostForm
#from django.urls import reverse_lazy

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	#ordering = ['-pub_date']
	#success_message = 'List successfully saved!!!!'

class SubmissionDetail(DetailView):
	model = Post
	template_name = 'submission_details.html'