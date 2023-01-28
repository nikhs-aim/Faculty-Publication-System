# Generated by Django 4.1.4 on 2023-01-28 15:56

import CSE.models
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0007_alter_faculty_fac_id_alter_post_post_snap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='fac_id',
            field=models.UUIDField(default=uuid.UUID('79d45ba1-b896-4f33-bf53-8d5798441ffb'), editable='false', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_snap',
            field=models.ImageField(default='default.jpg', upload_to='post_images/', validators=[CSE.models.validate_file_extension]),
        ),
    ]
