from django.urls import path

from . import views

urlpatterns = [
    # ex: books/
    path("", views.BookList.as_view(), name="create and view books"),
    
    # ex: books/{id}
    path(
        "<uuid:id>/", views.BookDetail.as_view(), name="get,update,delete books by id"
    ),
]
