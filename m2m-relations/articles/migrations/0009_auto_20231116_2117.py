# Generated by Django 3.1.2 on 2023-11-16 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_auto_20231116_2116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Tag',
            new_name='scopes',
        ),
    ]
