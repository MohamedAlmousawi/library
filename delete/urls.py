from . import views
from django.urls import path

urlpatterns = [
    path('<int:id>',views.delete,name='delete')
]