from django.conf.urls import url

from .views import (
    SearchView
)

# Search Applications URL Patterns

urlpatterns = [
    url(r'^search/$', SearchView.as_view(), name='search'),
]