# Generated by Django 3.1.2 on 2020-10-21 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_category_friendly_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]