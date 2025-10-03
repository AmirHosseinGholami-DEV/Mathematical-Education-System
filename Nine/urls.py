from django.urls import path
from . import views

urlpatterns = [
    # Home Url Path
    path("", views.NineHome.as_view(), name="Home Nine"),

    # Section Grade Path
    path("one/", views.OneView.as_view(), name="Nine Section One"),
    path("two/", views.TwoView.as_view(), name="Nine Section Two"),
    path("three/", views.ThreeView.as_view(), name="Nine Section Three"),
    path("four/", views.FourView.as_view(), name="Nine Section Four"),
    path("five/", views.FiveView.as_view(), name="Nine Section Five"),
    path("six/", views.SixView.as_view(), name="Nine Section Six"),
    path("seven/", views.SevenView.as_view(), name="Nine Section Seven"),
    path("eight/", views.EightView.as_view(), name="Nine Section Eight"),
    path("nine/", views.NineView.as_view(), name="Nine Section Nine"),

    # Section Grade Pdf Path
    path("one/pdf", views.Download_One.as_view(), name="Nine Section One pdf"),
    path("two/pdf", views.Download_Two.as_view(), name="Nine Section Two pdf"),
    path("three/pdf", views.Download_Three.as_view(), name="Nine Section Three pdf"),
    path("four/pdf", views.Download_Four.as_view(), name="Nine Section Four pdf"),
    path("five/pdf", views.Download_Five.as_view(), name="Nine Section Five pdf"),
    path("six/pdf", views.Download_Six.as_view(), name="Nine Section Six pdf"),
    path("seven/pdf", views.Download_Seven.as_view(), name="Nine Section Seven pdf"),
    path("eight/pdf", views.Download_Eight.as_view(), name="Nine Section Eight pdf"),
    path("nine/pdf", views.Download_Nine.as_view(), name="Nine Section Nine pdf"),
]
