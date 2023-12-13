from django.urls import path
from . import views

urlpatterns = [
    # ex: authors/
    path("", views.AuthorList.as_view(), name="create and view authors"),
    
    # ex: authors/{id}
    path(
        "<uuid:id>/", views.AuthorDetail.as_view(), name="get,update,delete authors by id"
    ),
]
