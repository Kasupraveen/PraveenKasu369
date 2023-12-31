# Generated by Django 3.0.5 on 2023-07-29 04:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0007_bookrequest_approved_by_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookrequest',
            name='requested_by_student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_requests_made', to=settings.AUTH_USER_MODEL),
        ),
    ]
