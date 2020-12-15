from django.urls import path

from truck import views

urlpatterns = [
    path('', views.login),
    path('owner_registration/', views.owner_registration),
    path('driver_recieve_portal/', views.driver_recieve_portal),
    path('comment/', views.comment),
    path('driver_pay_portal/', views.driver_pay_portal),
    path('add_vehicle/', views.add_vehicle),
    path('my_vehicles/', views.my_vehicle),
    path('vehicle_portal/<str:id>', views.vehicle_portal),
    path('view_statement/<str:id>', views.view_statement),
    path('change_password/', views.change_password),
    path('logout/', views.logout),
    path('username_checker/', views.username_checker),
]
