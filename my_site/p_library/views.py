from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from p_library.models import Author, Book, BookMaker


# Create your views here.
def books_list(request):
    books = Book.objects.all() 
    return HttpResponse(books) 

def index(request): 
    template = loader.get_template('index.html') 
    books = Book.objects.all() 
    biblio_data = {
        "title": "мою библиотеку",
        "books": books
    }
    return HttpResponse(template.render(biblio_data, request))

def bookmaker(request): 
    template = loader.get_template('index.html') 
    biblio = BookMaker.objects.all()
    return HttpResponse(template.render(biblio, request))

def publish(request, publish=False):
    output = "<h2>Product № {0}</h2>".format(publish)
    return HttpResponse(output)

def book_increment(request):
    if request.metod =='POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')

def book_decrement(request):
    if request.metod =='POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')