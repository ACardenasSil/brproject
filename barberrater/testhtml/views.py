from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import default_storage
import requests
import subprocess

# Create your views here.
def uploadimage(request):
    if request.method == 'POST':
        image_file = request.FILES['image']
        if default_storage.exists('TestImage.jpg'):
            default_storage.delete('TestImage.jpg')
        image_path = default_storage.save('TestImage.jpg', image_file)
        print('-----------')
        cmd = ['conda', 'activate', 'brenv', 'python', '~/brproject/face_classifier/face_shape_prediction.py', image_path]
        output = subprocess.run(cmd)
        print('==Face Output==')
        print(output)
        print('--End Output--')
        return HttpResponse('Image uploaded')
    return render(request, 'uploadimage.html')
