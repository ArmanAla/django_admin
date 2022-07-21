from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.db.models import Avg
from .models import Book


def index(request):
    books = Book.objects.all().order_by("title")
    books_count = books.count()
    avg_rating = books.aggregate(Avg("rating"))
    
    return (render(request, "book_outlet/index.html",{
        "books" : books,
        "total_number_of_books": books_count,
        "average_rating": avg_rating,
    }))


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404()
    
    book = get_object_or_404(Book, slug=slug)
    return(render(request, "book_outlet/book_detail.html",{
        "title" : book.title,
        "is_best_seller" : book.is_best_selling,
        "author" : book.author,
        "rating" : book.rating,
    }))
