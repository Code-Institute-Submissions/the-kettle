# Generated by Django 3.1.2 on 2020-10-20 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20201019_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('friendly_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
