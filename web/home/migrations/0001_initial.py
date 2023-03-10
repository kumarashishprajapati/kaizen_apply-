# Generated by Django 4.1.2 on 2022-11-16 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='apply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('department', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
                ('details', models.CharField(max_length=1000)),
                ('img1', models.ImageField(upload_to='images/')),
                ('img2', models.ImageField(upload_to='images/')),
                ('date', models.DateField()),
            ],
        ),
    ]
