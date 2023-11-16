from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='Book name')
    autor = models.CharField('Autor', max_length=50, default='Autor name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='user_books')

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/database/{self.id}'

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'