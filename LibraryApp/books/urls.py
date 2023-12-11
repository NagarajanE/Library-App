from django.urls import path

from . import views

urlpatterns = [
    # ex: books/
    path("", views.handle_book_request, name="create and view books"),
    
    # ex: books/{id}
    path(
        "<uuid:book_id>/", views.handle_book_by_id, name="get,update,delete books by id"
    ),
]
