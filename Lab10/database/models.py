from django.db import models


class Articles(models.Model):
    title = models.CharField('Name', max_length=50, default='Book name')
    autor = models.CharField('Autor', max_length=50, default='Autor name')
    anons = models.CharField('Anons', max_length=250, default='Description')
    full_text_pdf = models.FileField('Full_text_pdf', upload_to='articles_pdfs/', default="")
    quantity = models.IntegerField('Quantity', default=1)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/database/{self.id}'

    class Meta:
        verbose_name = 'article'
        verbose_name_plural = 'articles'