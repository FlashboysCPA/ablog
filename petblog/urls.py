from django.urls import path
#from . import views
from .views import HomeView, SubmissionDetail #, AddPostView, EditPostView, DeletePostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('submission/<int:pk>/', SubmissionDetail.as_view(), name='submission-detail'),
    #path('add_post/', AddPostView.as_view(), name='add_post'),
    #path('article/edit/<int:pk>/', EditPostView.as_view(), name='edit_post'),
    #path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
]