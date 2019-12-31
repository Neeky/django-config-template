"""djiangconfigtemplate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.shortcuts import render
from django.contrib import admin
from django.urls import path, include


# def view_404(request, exception, template_name=''):
#    return render(request, 'dct/index.html')

def main(request):
    return render(request, 'dct/index.html')


urlpatterns = [
    path('', main),
    path('admin/', admin.site.urls),
    path('exsample/', include('apps.exsample.urls'))
]

#handler404 = 'djiangconfigtemplate.urls.view_404'
#handler404 = 'djiangconfigtemplate.urls.view_404'
