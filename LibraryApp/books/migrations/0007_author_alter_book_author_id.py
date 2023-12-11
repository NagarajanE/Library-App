# Generated by Django 5.0 on 2023-12-11 05:33

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_book_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='id')),
                ('author_name', models.CharField(max_length=128, verbose_name='name')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='books.author'),
        ),
    ]