# Generated by Django 2.0.7 on 2018-07-11 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
    ]
