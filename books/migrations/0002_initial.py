# Generated by Django 3.2.20 on 2023-09-18 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='auther',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.auther'),
        ),
        migrations.AddField(
            model_name='bookauthor',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
