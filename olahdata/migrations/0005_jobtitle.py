# Generated by Django 3.0.5 on 2020-05-04 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahdata', '0004_wilayah'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobtitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('rumus', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]