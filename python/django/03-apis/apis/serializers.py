from rest_framework import serializers
from .models import books, Note, Hero, GeeksModel, Post, Comment, Staff   #import model
 
# Create a class
class booksSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = books
        fields = '__all__'

class noteSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Note
        fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Hero
        fields = '__all__'

class GeeksModelSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = GeeksModel
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Comment
        fields = '__all__'


class StaffSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Staff
        fields = '__all__'
