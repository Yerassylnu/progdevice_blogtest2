from django.db import models

class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок поста', max_length=100)
    description = models.TextField('Текст поста')
    author = models.CharField('Имя автора', max_length=100)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
