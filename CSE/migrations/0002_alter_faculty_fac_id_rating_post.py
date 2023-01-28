# Generated by Django 4.1.4 on 2023-01-28 14:04

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('147ebf05-c15a-4815-8848-b8a94721b16d'), editable='false', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('ratingName', models.CharField(max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('ratingComments', models.TextField(max_length=300)),
                ('ratingStars', models.CharField(blank=True, choices=[('up', 'Up vote'), ('down', 'Down Vote')], max_length=10, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ratingID', models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postTime', models.DateTimeField(auto_now_add=True)),
                ('postCategory', models.CharField(choices=[('Conference', 'Conference'), ('Journal', 'Journal')], max_length=50)),
                ('postSnaps', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='')),
                ('postTags', models.CharField(blank=True, max_length=200, null=True)),
                ('postID', models.ManyToManyField(blank=True, max_length=20, null=True, to=settings.AUTH_USER_MODEL)),
                ('ratings', models.ManyToManyField(blank=True, null=True, to='CSE.rating')),
            ],
        ),
    ]
