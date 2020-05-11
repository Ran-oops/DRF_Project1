"""helloworld URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from quickstartapp import views

#初始化一个路由对象， routers是drf里面的路由模块，DefaultRouter是默认路由器，是一个类，这里相当于是实例化产生一个
#叫router的路由对象。 路由时负责地址转发的
router=routers.DefaultRouter()

#对象调用register方法，里面有两个参数，r'users'对应网页url里面的users， 注册就激活了quickstartapp里面的views.py
#里面的UserViewSet类
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

#地址转发
urlpatterns = [
    url('admin/', admin.site.urls),
	url(r'^', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	
]
