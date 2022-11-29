from django.urls import path
from . import views

app_name='master'
urlpatterns =[
    path('home',views.master_home,name='master_home'),
    path('about',views.master_about,name='master_about'),
    path('blog',views.master_blog,name='master_blog'),
    path('portfolio',views.master_portfolio,name='master_portfolio'),
    path('contact',views.master_contact,name='master_contact'),
]
