from django.conf.urls import url
from booktest import views

# 通过url函数设置url路由配置项
urlpatterns = [
    url('^index$', views.index),  # 建立index/和视图index之间的联系
    url('^create$', views.create),
    url('^delete(\d+)$', views.delete),
]
