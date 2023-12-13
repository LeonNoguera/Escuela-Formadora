from django.urls import path
from . import views


urlpatterns=[
    path('',views.home, name="Vienvenidos"),
    path('res_1/',views.res_1, name="Residencia_1"),
    path('res_2/',views.res_2, name="Residencia_2"),
    path('res_3/',views.res_3, name="Residencia_3"),
    path('res_4/',views.res_4, name="Residencia_4"),
    path('res_5/',views.res_5, name="Residencia_5"),
    path('res_6/',views.res_6, name="Residencia_6"),

]