import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Book


# books/
@csrf_exempt
def handle_book_request(request):
    if request.method == "GET":
        return get_all_books()
    elif request.method == "POST":
        return create_book(request)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_all_books():
    booksFetched = Book.objects.all()
    response = ""
    for book in booksFetched:
        response += "<h1> {} </h1>".format(book)
    return HttpResponse(response)


@csrf_exempt
def create_book(request):
    data = request_json_helper(request)

    name = data["name"]
    author_id = data["author_id"]
    initial_copies = data["initial_copies"]

    book = Book(book_name=name, author_id=author_id, copies_count=initial_copies)
    book.save()
    return HttpResponse("Book added")


# books/{id}
@csrf_exempt
def handle_book_by_id(request, book_id):
    print(request.method)
    if request.method == "DELETE":
        return delete_book_by_id(book_id)
    elif request.method == "GET":
        return get_book_by_id(book_id)
    elif request.method == "PUT":
        return update_book_by_id(request, book_id)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_book_by_id(book_id):
    bookFetched = Book.objects.get(book_id=book_id)
    return HttpResponse("<h1> {} </h1>".format(bookFetched))


@csrf_exempt
def update_book_by_id(request, book_id):
    data = request_json_helper(request)

    name = data["name"]
    author_id = data["author_id"]
    initial_copies = data["initial_copies"]

    fetchedBook = Book.objects.get(book_id=book_id)
    fetchedBook.book_name = name
    fetchedBook.author_id = author_id
    fetchedBook.copies_count = initial_copies
    fetchedBook.save()
    return HttpResponse("Book Updated")


@csrf_exempt
def delete_book_by_id(book_id):
    try:
        bookFetched = Book.objects.get(book_id=book_id)
        bookFetched.delete()
        return HttpResponse("Books Deleted")
    except:
        return HttpResponse("Error Deleting Book")


def request_json_helper(request):
    raw_data = request.body.decode("utf-8")
    try:
        data = json.loads(raw_data)
        return data
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
