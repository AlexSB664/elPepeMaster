"""elPepeMaster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib.auth.views import logout_then_login

#para las fotos
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from principal.views import acercadeP, registroU,Index,dashboard
from principal import views
from files.views import upload_file
from filebrowser.sites import site
"""
from pagina import views
from pagina.views import acercadeP
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^admin/filebrowser/',site.urls),
    url(r'^$',views.Index, name='index'),
    #url(r'index$',views.Index, name='index'),
    path('index/', Index,name='index'),     
    path('acercade/', acercadeP,name='acercade'), 
    path('registro/', registroU,name='registro'),
    url(r'^dashboard', dashboard, name='dashboard'),
    url(r'^uploads/', upload_file, name="uploads"),

]

#para las fotos
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
