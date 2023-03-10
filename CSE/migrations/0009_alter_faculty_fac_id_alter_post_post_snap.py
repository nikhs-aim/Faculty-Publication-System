# Generated by Django 4.1.4 on 2023-01-28 16:05

import CSE.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0008_alter_faculty_fac_id_alter_post_post_snap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('c68bcf6e-81fd-4822-b980-5c3de48aa501'), editable='false', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_snap',
            field=models.ImageField(upload_to='post_images/', validators=[CSE.models.validate_file_extension]),
        ),
    ]
