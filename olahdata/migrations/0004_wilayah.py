# Generated by Django 3.0.5 on 2020-05-04 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olahdata', '0003_auto_20200430_1059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desa', models.CharField(max_length=200, null=True)),
                ('kec', models.CharField(max_length=200, null=True)),
                ('kota', models.CharField(max_length=200, null=True)),
                ('provinsi', models.CharField(max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
