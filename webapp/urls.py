from django.urls import path
from .views import (index_view,
                    about_view,
                    contacts_view)

app_name = 'webapp'
urlpatterns = [
    path(r'', index_view, name='home'),
    path(r'about/', about_view, name='about'),
    path(r'contacts/', contacts_view, name='contacts'),
]
