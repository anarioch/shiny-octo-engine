from django.urls import path

from . import views

urlpatterns = [
    path("companies/<int:company_id>", views.company, name="company"),
]
