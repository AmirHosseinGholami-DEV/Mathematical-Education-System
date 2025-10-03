from django.urls import path
from . import views

urlpatterns = [
    # Home Url Path
    path("", views.SevenHome.as_view(), name="Home Seven"),

    # Section Grade Path
    path("one/", views.OneView.as_view(), name="Seven Section One"),
    path("two/", views.TwoView.as_view(), name="Seven Section Two"),
    path("three/", views.ThreeView.as_view(), name="Seven Section Three"),
    path("four/", views.FourView.as_view(), name="Seven Section Fore"),
    path("five/", views.FiveView.as_view(), name="Seven Section Five"),
    path("six/", views.SixView.as_view(), name="Seven Section Six"),
    path("seven/", views.SevenView.as_view(), name="Seven Section Seven"),
    path("eight/", views.EightView.as_view(), name="Seven Section Eight"),
    path("nine/", views.NineView.as_view(), name="Seven Section Nine"),

    # Section Grade Pdf Path
    path("one/pdf", views.Download_One.as_view(), name="Seven Section One pdf"),
    path("two/pdf", views.Download_Two.as_view(), name="Seven Section Two pdf"),
    path("three/pdf", views.Download_Three.as_view(), name="Seven Section Three pdf"),
    path("four/pdf", views.Download_Four.as_view(), name="Seven Section Fore pdf"),
    path("five/pdf", views.Download_Five.as_view(), name="Seven Section Five pdf"),
    path("six/pdf", views.Download_Six.as_view(), name="Seven Section Six pdf"),
    path("seven/pdf", views.Download_Seven.as_view(), name="Seven Section Seven pdf"),
    path("eight/pdf", views.Download_Eight.as_view(), name="Seven Section Eight pdf"),
    path("nine/pdf", views.Download_Nine.as_view(), name="Seven Section Nine pdf"),
]