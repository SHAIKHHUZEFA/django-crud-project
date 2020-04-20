from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.first,name="first"),
    path('create',views.create,name="create"),
    path('update/<int:id>',views.update,name="update"),
    path('edit',views.save_product,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
]

