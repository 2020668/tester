from django.conf.urls import url
from booktest import views

# 通过url函数设置url路由配置项
urlpatterns = [
    url('^index$', views.index),  # 建立index/和视图index之间的联系
    url('^create$', views.create),
    url('^delete(\d+)$', views.delete),
    # url('^showarg(\d+)$', views.show_arg),       # 位置参数
    url('^showarg(?P<num>\d+)$', views.show_arg),       # 关键字参数
    url('^login$', views.login),
    url('^login_check$', views.login_check),
    url('^test_ajax$', views.ajax_test),    # 显示ajax页面
    url('^ajax_handle$', views.ajax_handle),    # ajax处理
    url('^login_ajax$', views.login_ajax),       # 显示ajax登录页面
    url('^login_ajax_check$', views.login_ajax_check),    # ajax登录校验
    url('^set_cookie$', views.set_cookie),    # 设置cookie
    url('^get_cookie$', views.get_cookie)    # 获取cookie
]
