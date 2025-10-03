from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("video/", views.VideoView.as_view(), name="Video"),
    path("about/", views.AboutView.as_view(), name="About"),
    path("ai/", views.AiView.as_view(), name="ai"),
    path("education", views.EducationView.as_view(), name="Education System"),
    path("login/", views.login_view, name="Login Page"),
    path("logout/", views.logout_view, name="Logout"),
    path('signup/', views.SignUpView.as_view(), name='register'),
    path("stem/", views.StemView.as_view(), name="Stem"),
]
