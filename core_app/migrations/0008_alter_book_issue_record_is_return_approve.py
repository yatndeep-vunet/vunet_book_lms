# Generated by Django 5.1 on 2024-08-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0007_remove_book_issue_record_is_return_applied_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_issue_record',
            name='is_return_approve',
            field=models.BooleanField(null=True),
        ),
    ]
