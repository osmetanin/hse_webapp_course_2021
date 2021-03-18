from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_blog_list, name="index"),
    path('<int:blog_id>', views.blog, name="blog_by_id"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('signup', views.sign_up, name="signup"),
]