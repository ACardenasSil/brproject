"""barberrater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.static import serve
from api.views import *
from serveflutter.views import *
from testhtml.views import *

# https://stackoverflow.com/questions/61582897/how-to-serve-a-flutter-web-app-with-django
# flutter_redirect() allows flutter files to be served at the requested url 
Flutter_app_loc = '../BarberRater/flutter_baberrater/build/web'
def flutter_redirect(request, resource):
        return serve(request, resource, Flutter_app_loc)

urlpatterns = [
    path('/admin/', admin.site.urls),
    path('/image/', index_view),
    path('/app/', serve_flutter_app),
    path('/timage/', uploadimage),
    path('/', lambda r: serve(r, 'index.html', Flutter_app_loc)), 
    path('/<path:resource>', flutter_redirect) 
]
