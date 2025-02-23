# Generated by Django 5.1.6 on 2025-02-23 15:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0004_book_created_by_book_genre_book_isbn_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a new book'), ('can_edit_book', 'Can edit book details'), ('can_delete_book', 'Can delete a book')]},
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship_app.author'),
        ),
    ]
