from django.urls import path

from . import views

urlpatterns = [
    path("<int:company_id>", views.index, name="index"),
]
