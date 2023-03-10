# Generated by Django 4.1.4 on 2023-01-28 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0003_remove_rating_ratingid_alter_faculty_fac_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('9e431295-3b8a-41ba-ade4-27f970023b48'), editable='false', primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=300)),
                ('post_snap', models.ImageField(upload_to='post_images/')),
                ('post_details', models.TextField(max_length=1000)),
                ('post_time', models.DateTimeField(auto_now_add=True)),
                ('post_category', models.CharField(choices=[('conference', 'conference'), ('journal', 'journal')], max_length=100)),
                ('fac_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
