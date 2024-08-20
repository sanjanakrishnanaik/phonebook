from django.contrib import admin
from django.urls import path, include

from contacts.views import contact_create, contact_delete, contact_detail, contact_update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacts.urls')),
    path('<int:pk>/', contact_detail, name='contact_detail'),
    path('add/', contact_create, name='contact_create'),
    path('<int:pk>/edit/', contact_update, name='contact_update'),
    path('<int:pk>/delete/', contact_delete, name='contact_delete'),
]
