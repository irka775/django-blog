# Generated by Django 4.2.13 on 2024-06-04 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_comment_challenge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='challenge',
        ),
    ]
