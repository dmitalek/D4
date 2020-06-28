from django.contrib import admin
from p_library.models import Book, Maker, BookMaker

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'price')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publisher')
    


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    @staticmethod
    def maker_name(obj):
        return obj.Maker.make_name

    list_display = ('make_name', 'make_country')
    fields = ('make_name', 'make_country' )

@admin.register(BookMaker)
class BookMakerAdmin(admin.ModelAdmin):
    @staticmethod
    def bookmaker_name(obj):
        return obj.BookMaker.publisher

    list_display = ('publisher', 'book', 'year')
    fields = ('publisher', 'book', 'year')