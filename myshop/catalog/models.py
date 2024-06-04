from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя', help_text='Введите имя автора')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия', help_text='Введите фамилию автора')
    slug = models.SlugField(max_length=250, unique=True, verbose_name='URL-адрес')
    photo = models.ImageField(upload_to='author_photos/', blank=True, null=True, verbose_name='Фотография')
    biography = models.TextField(verbose_name='Биография', help_text='Краткая биография автора', blank=True)


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название', help_text="Введите название книги")
    isbn = models.CharField(max_length=17, verbose_name='ISBN')
    cover = models.ImageField(upload_to='cover_images/', blank=True, verbose_name='Обложка')
    description = models.TextField(blank=True, verbose_name='Описание')
    year = models.PositiveIntegerField(verbose_name='Год издания')
    language = models.CharField(max_length=100, blank=True, verbose_name='Язык')
    publisher = models.CharField(max_length=200, blank=True, null=True, verbose_name='Издательство')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name='Цена')
    is_available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
