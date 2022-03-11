"""config URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qnaboard/', include('qnaboard.urls')),
    path('users/', include('users.urls')),
    path('challenges/', include('challenges.urls')),
    path('bigday/', include('bigday.urls')),
    path('study/', include('study.urls')),
    path('map/', include('map.urls')),
    path('competition/', include('competition.urls')),
    path('group/', include('group.urls')),
]

# 프로덕션 모드인지 개발 모드인지 검사 - debug 모드가 켜져있는지 확인 하고 이미지의 url을 static 으로 변경함
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
