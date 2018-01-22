from django.shortcuts import render

# Create your views here.
def book_index(request):
    return render(request, 'book_index.html')
