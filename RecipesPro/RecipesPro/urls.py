from django.contrib import admin
from django.urls import path
from recipesapp import views
app_name = 'recipesapp'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name= 'home'),
    path('home/', views.home, name= 'home'),
    path('creatobj/', views.creatobj, name = 'creatobj'),
    path('<int:id>/', views.delete, name = 'delete'),
    path('<int:id>/', views.details, name = 'details'),
]
