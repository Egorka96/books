from django.db import models


class Author(models.Model):
    name = models.CharField("Имя автора", max_length=100)
    contacts = models.CharField('Контакты', max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField('Название', max_length=100)
    pub_date = models.DateField('Дата издания')

    def __str__(self):
        return self.title
