from django.urls import path
from . import views
urlpatterns = [
    path(r'', views.index,name='index'),
    path(r'base_layout',views.base_layout,name='base_layout'),
    path(r'getdata',views.getdata,name='getdata'),
    path(r'csv',views.import_csv,name='import_csv'),
    path(r'getmeter',views.getmeter,name='getmeter'),
    path(r'meter',views.meter,name='meter'),
    path(r'index_posts',views.index_posts,name='index_posts'),
]