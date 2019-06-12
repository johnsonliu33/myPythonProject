# -*- coding:utf-8 -*-
"""Django_Restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path  # 路径模块
from django.conf.urls import include  # 控制添加路径的模块
from rest_framework import routers  # 路由配置模块
from api import views
# 导入辅助函数get_schema_view
from rest_framework.schemas import get_schema_view
# 导入两个类
from rest_framework_swagger.renderers import SwaggerUIRenderer, OpenAPIRenderer

router = routers.DefaultRouter()  # 创建路由对象
router.register('users', views.UserViewSet)  # 调用register方法，配置Users的路由
router.register('groups', views.GroupViewSet)  # 配置Groups路由

# 利用辅助函数引入所导入的两个类
schema_view = get_schema_view(title='API', renderer_classes=[SwaggerUIRenderer, OpenAPIRenderer])

# 配置url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # 代表位于根路径的主域名(http://127.0.0.1:8000)
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # api-auth对应授权登录url
    path('docs/', schema_view, name='docs')  # 配置docs的url路径
]
