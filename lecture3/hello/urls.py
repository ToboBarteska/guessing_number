from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:promena>/<str:cena>",views.problem, name="problem"),
    path("pohoda",views.pohoda, name="pohoda")
]