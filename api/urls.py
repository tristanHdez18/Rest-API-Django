from django.urls import path
from django.urls.resolvers import URLPattern
from .views import CommpanyView

urlpatterns=[
    path('companies/', CommpanyView.as_view(), name='companies_list'),
    path('companies/<int:id>', CommpanyView.as_view(), name='companies_process')
]