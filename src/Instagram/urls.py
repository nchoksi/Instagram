"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib import admin
from profiles import views as profile_views
from images import views as images_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('allauth.urls')),
    url(r'^$', profile_views.dashboard, name='dashboard'),
    url(r'^home/', images_views.home, name='home'),

    # Crud on User profile
    url(r'^account/edit/$', profile_views.edit, name='edit'),

    # Image Upload
    url(r'^images/', include('images.urls', namespace='images')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)