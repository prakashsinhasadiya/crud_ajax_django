"""single_page URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from crud import views as crud_views
from django.conf import settings

app_name = 'crud'


urlpatterns = [
    url(r'^$', crud_views.form, name='form'),
    url(r'^admin/', admin.site.urls),
    url(r'^submit/$', crud_views.submit, name='submit'),
    url(r'^edit/$', crud_views.edit, name='edit'),
    # url(r'^student/(?P<id>[^/]*)/edit$', crud_views.edit, name='edit'),
    # url(r'^student/(?P<id>[^/]*)/delete$', crud_views.delete, name='delete'),


    url(r'^delete/$', crud_views.delete, name='delete'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
