# Generated by Django 4.2.7 on 2023-11-05 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_articles_date_remove_articles_full_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='anons',
            field=models.CharField(default='Description', max_length=250, verbose_name='Anons'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='autor',
            field=models.CharField(default='Autor name', max_length=50, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(default='Book name', max_length=50, verbose_name='Name'),
        ),
    ]
