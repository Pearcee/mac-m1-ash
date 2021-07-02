from django.contrib import admin
from django.urls import path
 
from apis import views #import views
 
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.booklist.as_view()),
    path('notes/', views.notelist.as_view()),
    path('hero/', views.Herolist.as_view()),
    path('geeksmodel/', views.GeeksModellist.as_view()),
    path('post/', views.Postlist.as_view()),
    path('comment/', views.Commentlist.as_view()),
    path('staff/', views.Stafflist.as_view()),    
]
 

""" 

 Hero, GeeksModel, Post, Comment, Staff
  """