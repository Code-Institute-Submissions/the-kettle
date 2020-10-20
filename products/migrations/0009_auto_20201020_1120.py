# Generated by Django 3.1.2 on 2020-10-20 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('friendly_name', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='friendly_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
