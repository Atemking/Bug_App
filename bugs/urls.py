from django.urls import path

from . import views

app_name = "bugs"

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/",views.contact_page_view , name = "contact_page_view"),
    path("register", views.register, name="register"),
    path('display',views.TableView.as_view(),name='table'),
   
]