# Generated by Django 5.0.4 on 2024-05-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_tag_book_catecogy_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='data_created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]