# Generated by Django 4.2.13 on 2024-06-04 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_comment_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='challenge',
            field=models.SlugField(),
        ),
    ]
