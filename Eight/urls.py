from django.urls import path
from . import views

urlpatterns = [
    # Home Url Path
    path("", views.EightHome.as_view(), name="Home Eight"),

    # Section Grade Path
    path("one/", views.OneView.as_view(), name="Eight Section One"),
    path("two/", views.TwoView.as_view(), name="Eight Section Two"),
    path("three/", views.ThreeView.as_view(), name="Eight Section Three"),
    path("four/", views.FourView.as_view(), name="Eight Section Fore"),
    path("five/", views.FiveView.as_view(), name="Eight Section Five"),
    path("six/", views.SixView.as_view(), name="Eight Section Six"),
    path("seven/", views.SevenView.as_view(), name="Eight Section Seven"),
    path("eight/", views.EightView.as_view(), name="Eight Section Eight"),
    path("nine/", views.NineView.as_view(), name="Eight Section Nine"),

    # Section Grade Pdf Path
    path("one/pdf", views.Download_One.as_view(), name="Eight Section One pdf"),
    path("two/pdf", views.Download_Two.as_view(), name="Eight Section Two pdf"),
    path("three/pdf", views.Download_Three.as_view(), name="Eight Section Three pdf"),
    path("three/islam/pdf", views.Download_Three_Islam.as_view(), name="Eight Section Three islam pdf"),
    path("four/pdf", views.Download_Four.as_view(), name="Eight Section Four pdf"),
    path("five/pdf", views.Download_Five.as_view(), name="Eight Section Five pdf"),
    path("six/pdf", views.Download_Six.as_view(), name="Eight Section Six pdf"),
    path("seven/pdf", views.Download_Seven.as_view(), name="Eight Section Seven pdf"),
    path("eight/pdf", views.Download_Eight.as_view(), name="Eight Section Eight pdf"),
    path("nine/pdf", views.Download_Nine.as_view(), name="Eight Section Nine pdf"),
    
]
