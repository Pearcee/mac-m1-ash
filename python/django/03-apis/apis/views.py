from django.shortcuts import render
 
# Create your views here.
 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import books, Note, Hero, GeeksModel, Post, Comment, Staff
from .serializers import booksSerializer, noteSerializer, HeroSerializer, GeeksModelSerializer, PostSerializer, CommentSerializer, StaffSerializer
 
 
class booklist(APIView):
 
    def get(self,request):
        book1 = books.objects.all()
        serializer = booksSerializer(book1, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass

class notelist(APIView):
 
    def get(self,request):
        oall = Note.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass

class Herolist(APIView):
 
    def get(self,request):
        oall = Hero.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass

class GeeksModellist(APIView):
 
    def get(self,request):
        oall = GeeksModel.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass
         
class Postlist(APIView):
 
    def get(self,request):
        oall = Post.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass
  
class Commentlist(APIView):
 
    def get(self,request):
        oall = Comment.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass
  
class Stafflist(APIView):
 
    def get(self,request):
        oall = Staff.objects.all()
        serializer = noteSerializer(oall, many= True)
        return Response(serializer.data) # Return JSON
 
    def post(self):
        pass
  
