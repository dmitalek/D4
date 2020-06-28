from django.utils.translation import gettext as _  
from django.db import models
  
class Author(models.Model):  
    full_name = models.TextField(verbose_name=_("Имя автора"))
    birth_year = models.SmallIntegerField(verbose_name=_("Год рождения"))
    country = models.CharField(max_length=2, verbose_name=_("Страна"))

    def __str__(self):
        return self.full_name

class Maker(models.Model):  
    make_name = models.TextField(default=None, verbose_name=_("Название издательства"))
    make_country = models.CharField(max_length=2, verbose_name=_("Страна издательства"))
      
    def __str__(self):
        return self.make_name

class Book(models.Model):
    ISBN = models.CharField(max_length=13)  
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Автор'), related_name='book_author')
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(default=None, max_digits=8, decimal_places=2)
    maker = models.ForeignKey(Maker, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_('Издательство'), related_name='book_pub')
    
    def __str__(self):
	    return self.title

class BookMaker(models.Model):  
    book = models.ForeignKey('p_library.Book', default=None, on_delete=models.CASCADE, verbose_name=_('Издательство'), related_name='publish_house')
    publisher = models.ForeignKey('p_library.Maker', default=None, on_delete=models.CASCADE, verbose_name=_('Издательство'), related_name='publish_house')
    year = models.ForeignKey('p_library.Book', default=None, on_delete=models.CASCADE, verbose_name=_('Год издания'), related_name='publish_year')
    
    def __str__(self):
        return self.publisher