# Generated by Django 2.2.3 on 2019-07-02 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=20)),
                ('sym', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
