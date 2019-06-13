# -*- coding:utf-8 -*-

# from django.contrib.auth.models import User, Group #django默认数据库
from api.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")  # 第一个参数必须是URL
