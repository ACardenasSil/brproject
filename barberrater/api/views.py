from django.shortcuts import render
from django.http import HttpResponse, FileResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from django.core.files.storage import default_storage
import os
import sys
import requests
import subprocess
import random
import json
import urllib.parse
# Create your views here.

def index_view(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        if default_storage.exists('faceimage.jpg'):
            default_storage.delete('faceimage.jpg')
        image_path = default_storage.save('faceimage.jpg', image_file)
        print('-------')
        script_path = '/home/alonso/brproject/face_classifier/'
        faceshape = open('/home/alonso/brproject/face_classifier/faceshape','r')
        cmd = ['python3', script_path+'face_shape_prediction.py', image_path]
        shape_output = subprocess.run(cmd)


        shape = faceshape.read()
        #print(shape)
        #print('==End Output==')

        shape_file = open(script_path+'faceshape', 'r')
        shape = shape_file.read()
        gender = 'male'
        file_dir = script_path+'styles/'+gender+'/'+shape+'/'
        hair_file_name = random.choice(os.listdir(file_dir))
        hair_file_path = file_dir+hair_file_name
        hair_file = open(hair_file_path, 'rb')
        hair_data = { 
                'file_name': hair_file_name ,
                'face_shape': shape ,
                }
        
        #HttpResponse help from 
        # https://docs.djangoproject.com/en/4.2/ref/request-response/
        # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
        response = JsonResponse(status=200, data=hair_data)

        return response
    return HttpResponse("--Only POST requests please") 
