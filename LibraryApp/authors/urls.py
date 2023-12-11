from django.urls import path
from . import views

urlpatterns = [
    # ex: authors/
    path("", views.handle_author_request, name="create and view authors"),
    
    # ex: authors/{id}
    path(
        "<uuid:author_id>/", views.handle_author_by_id, name="get,update,delete authors by id"
    ),
]
