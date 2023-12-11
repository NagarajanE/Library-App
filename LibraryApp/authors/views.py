import json
from django.http import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Author


# authors/
@csrf_exempt
def handle_author_request(request):
    if request.method == "GET":
        return get_all_authors()
    elif request.method == "POST":
        return create_author(request)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_all_authors():
    author_fetched = Author.objects.all()
    response = ""
    for author in author_fetched:
        response += "<h1> {} </h1>".format(author)
    return HttpResponse(response)


@csrf_exempt
def create_author(request):
    data = request_json_helper(request)
    name = data["name"]
    author = Author(author_name=name)
    author.save()
    return HttpResponse("<h1>author added</h1>")


# authors/{id}
@csrf_exempt
def handle_author_by_id(request, author_id):
    print(request.method)
    if request.method == "DELETE":
        return delete_author_by_id(author_id)
    elif request.method == "GET":
        return get_author_by_id(author_id)
    elif request.method == "PUT":
        return update_author_by_id(request, author_id)
    else:
        return JsonResponse({"error": "Unsupported method"}, status=405)


def get_author_by_id(author_id):
    author_fetched = Author.objects.get(author_id=author_id)
    return HttpResponse("<h1> {} </h1>".format(author_fetched))


@csrf_exempt
def update_author_by_id(request, author_id):
    data = request_json_helper(request)

    name = data["name"]
    author_fetched = Author.objects.get(author_id=author_id)
    author_fetched.author_name = name
    author_fetched.save()
    return HttpResponse("author Updated")


@csrf_exempt
def delete_author_by_id(author_id):
    try:
        author_fetched = Author.objects.get(author_id=author_id)
        author_fetched.delete()
        return HttpResponse("authors Deleted")
    except:
        return HttpResponse("Error Deleting author")


def request_json_helper(request):
    raw_data = request.body.decode("utf-8")
    try:
        data = json.loads(raw_data)
        return data
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)
