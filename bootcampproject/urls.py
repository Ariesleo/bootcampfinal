"""bootcampproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

import projectlist.views

urlpatterns = [

    path('', projectlist.views.addproject, name='addproject'),
    path('adduser/',projectlist.views.adduser, name='adduser'),
    path('showprojectlist/',projectlist.views.showprojectlist, name='showprojectlist'),
    path('addarticle/', projectlist.views.addarticle, name='addarticle'),
    path('showarticle/',projectlist.views.showarticle, name='showarticle'),
    path('update_list/<str:pk>/', projectlist.views.listupdate, name='update_list'),
    path('update_feedback/<str:pk>/', projectlist.views.feedbackupdate, name='update_feedback'),
    path('delete_project/<str:pk>/', projectlist.views.projectdelete, name='delete_project'),
    path('update_article/<str:pk>/', projectlist.views.updatearticle, name='update_article'),
    path('delete_card/<str:pk>/', projectlist.views.cardDelete, name='delete_card'),
    path('update_user/<str:pk>/', projectlist.views.updateUsers , name='update_user'),
    path('delete_user/<str:pk>/', projectlist.views.Userdelete, name='delete_user'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
