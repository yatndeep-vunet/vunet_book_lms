# Generated by Django 5.1 on 2024-08-25 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0005_librarian'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_issue_record',
            name='is_return_applied',
            field=models.BooleanField(default=False),
        ),
    ]
