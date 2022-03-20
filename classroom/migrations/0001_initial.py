# Generated by Django 3.2.7 on 2022-03-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classrooom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=30)),
                ('room', models.CharField(max_length=30)),
                ('teacher', models.CharField(max_length=50)),
                ('class_code', models.CharField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='classroom_gallery/')),
            ],
        ),
    ]
