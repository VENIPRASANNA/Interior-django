# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('index.html/', views.index, name='index'),
    path('design.html/', views.design, name='design'),
    path('contact.html/', views.contact, name='contact'),
    path('int1.html/', views.int1, name='int1'),
    path('int2.html/', views.int2, name='int2'),
    path('offer1.html/', views.offer, name='offer'),
    path('order.html/', views.order, name='order'),
    path('project.html/', views.project, name='project'),
    path('recent.html/', views.recent, name='recent'),
    path('req.html/', views.req, name='req'),
    path('design.html/req.html/', views.req,name='req'),
    path('design.html/req.html/order.html', views.order,name='order'),
    path('project.html/recent.html', views.recent, name='recent'),
    path('project.html/int.html',views.int1,name='int1'),
    path('project.html/int2.html',views.int2,name='int2'),
    path('project.html/int1.html/req.html,',views.req,name='req'),
    path('project.html/int2.html/req.html,',views.int2,name='int2'),
    path('project.html/int1.html/req.html/order.html', views.order, name='order'),
    path('project.html/int2.html/req.html/order.html', views.order, name='order')
    # path("index.html/",views.index, name='index')
]
