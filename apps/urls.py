"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('_nested_admin/', include('nested_admin.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', include(('lk.urls','lk'),namespace='lk')),
    path('quiz/', include(('quiz.urls', 'quiz'), namespace='quiz')),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
    path('news/',include(('news.urls','news'),namespace='news')),

    path('user/', include('users.urls')),
    path('chat/', include('privatmessages.urls')),
    path('autf/', include('users.urls')),
    path('chat2/',include('chanelmessages.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

]


# path('auth/', include('djoser.urls')),
# path('auth/', include('djoser.urls.jwt')),
# path('auth/', include('djoser.urls.authtoken')),


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
