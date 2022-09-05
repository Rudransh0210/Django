from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
import Crypto.Hash import SHA256
from backend.models import backend
from .serializer import BackendSerializer
from rest_framework.decorators import api_view
import json


# Create your views here.

def index(request):
    user = request.COOKIES.get('user')
    password = request.COOKIES.get('pwd')
    loggedin = request.COOKIES.get('loggedin')
    if user == "admin" and password == SHA256.new(b"admin").hexdigest() and loggedin == "true":
        response = HttpResponse(json.dumps({"status": "loggedin"}))
        return response
    response = HttpResponse()
    response.set_cookie('user', None)
    response.set_cookie('pwd', None)
    response.set_cookie('loggedin', None)
    return response

@api_view(['POST'])
def addblog(request):
    data = json.dumps(request.data)
    if ('username' not in data) or ('password' not in data):
        return HttpResponse("Please enter username and password")
    blogdata = BackendSerializer(data = request.data)
    data = json.loads(data)
    user = data['username']
    pwd = data['password']
    if user == "admin" and pwd == SHA256.new(b"admin").hexdigest():
        if blogdata.is_valid():
            blogdata.save()
            return HttpResponse("Blog added successfully")
        else:
            return HttpResponse("Invalid data")
    return HttpResponse("Wrong username or password")

@api_view(['GET'])
def getblogs(request):
    qs_json = serializers.serialize('json', backend.objects.all())
    print(qs_json)
    return HttpResponse(qs_json, content_type='application/json')

@api_view(['POST'])
def deleteblog(request):
    data = json.dumps(request.data)
    if ('username' not in data) or ('password' not in data):
        return HttpResponse("Please enter username and password")
    data = json.loads(data)
    user = data['username']
    pwd = data['password']
    if user == "admin" and pwd == SHA256.new(b"admin").hexdigest():
        pk = data['pk'] #delete using primary key
        dblog = backend.objects.filter(pk=pk)
        if (dblog == None):
            return HttpResponse("Blog not found")
        try:
            blogdata = serializers.serialize('json', dblog)
            dblog.delete()
            return HttpResponse("Deleted successfully")        
        except:
            return HttpResponse("Error occurred, please try again")
    return HttpResponse("Unauthorized")

@api_view(['POST'])
def updateblog(request):
    data = json.dumps(request.data)
    if ('username' not in data) or ('password' not in data):
        return HttpResponse("Please enter username and password")
    data = json.loads(data)
    user = data['username']
    pwd = data['password']
    if user == "admin" and pwd == SHA256.new(b"admin").hexdigest():
        pk = data['pk']
        ublog = backend.objects.filter(pk=pk)
        if (ublog == None):
            return HttpResponse("Blog not found")
        if (('title' not in data) or ('content' not in data)):
            return HttpResponse("Invalid data")
        try:
            ublog.update(title=data['title'], content=data['content'])
            return HttpResponse(serializers.serialize('json', ublog), content_type='application/json')
        except:
            return HttpResponse("Error occurred, please try again")
    return HttpResponse("Unauthorized")

@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    print(data)
    if ('username' not in data) or ('password' not in data):
        return HttpResponse("Please enter username and password")
    user = data['username']
    pwd = data['password']
    if user == "admin" and pwd == SHA256.new(b"admin").hexdigest():
        response = HttpResponse(json.dumps({"status": "loggedin", "user": user, "password": pwd}))
        response.set_cookie('user', user)
        response.set_cookie('pwd', pwd)
        response.set_cookie('loggedin', 'true')
        return response
    return HttpResponse(json.dumps({"status": "failed"}))