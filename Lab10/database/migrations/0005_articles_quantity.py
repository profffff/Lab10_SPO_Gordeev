# Generated by Django 4.2.7 on 2023-11-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_alter_articles_anons_alter_articles_autor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='quantity',
            field=models.IntegerField(default=1, verbose_name='Quantity'),
        ),
    ]
