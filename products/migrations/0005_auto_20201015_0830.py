# Generated by Django 3.1.2 on 2020-10-15 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20201014_1722'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tea',
            old_name='leaf_type',
            new_name='ingredients',
        ),
    ]
