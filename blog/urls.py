from django.urls import path
from .views import index, blog_detail ,blog_yarat, blog_taxrirlash,blog_ochrish,signub
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView,PasswordChangeDoneView
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView,PasswordResetDoneView,PasswordResetCompleteView
urlpatterns = [
    path("",index,name='index'),
    path('login/',LoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path("signup/", signub, name="signup"),
    path('blog/<int:blog_id>/',blog_detail,name="blog_detail"),
    path("blog_yarat/",blog_yarat,name='blog_yarat'),
    path("blog_taxrirlash/<int:blog_id>/",blog_taxrirlash,name='blog_taxrirlash'),
    path("blog_ochirish/<int:blog_id>/",blog_ochrish,name='blog_ochirish'),
    path("password/change/",PasswordChangeView.as_view(template_name='registration/password.html'), name='password_change'),
    path("password-change-done/",PasswordChangeDoneView.as_view(template_name='registration/password_done.html'),name='password_change_done'),
    path("password-reset/",PasswordResetView.as_view(template_name='registration/pass_confirm.html',),name='password_reset_confirm'),
    path("password-reset/confirm/",PasswordResetConfirmView.as_view(template_name='registration/pass_reset_done.html'),name='password_reset_done'),
     path("password-reset/complete/",PasswordResetCompleteView.as_view(template_name='registration/pass_reset_complete.html'),name='password_reset_complete'),
] 