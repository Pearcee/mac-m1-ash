from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UsersList.as_view()),
    path('users/<int:pk>/', views.UsersDetail.as_view()),    
    path(r'index_users',views.index_users,name='index_users'),
]

urlpatterns = format_suffix_patterns(urlpatterns)