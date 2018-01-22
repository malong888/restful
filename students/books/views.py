from django.shortcuts import render
from books.models import Book
from django.http import JsonResponse
# Create your views here.
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        books = [{'id': b.id, 'name': b.name} for b in books]

        return JsonResponse(books, safe=False) # safe=False允许JsonResponse序列化list

    if request.method == 'POST':
        name = request.POST.get('name')

        book = Book(name=name)
        book.save()

        return JsonResponse({'code': 200, 'msg': 'post ok!'})
