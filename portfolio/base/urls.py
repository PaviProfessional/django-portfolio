from django.urls import path
from . import views

urlpatterns = [
    path('',views.contact,name="contact"),
    path('contact/',views.letstalk,name="letstalk"),
    path('youtube/',views.youtube,name="youtube"),
    path('ecommerce/',views.ecommerce,name="ecommerce"),
    path('myportfolio/',views.portfolio,name="portfolio"),

]
