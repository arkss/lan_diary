# Generated by Django 2.0.7 on 2018-08-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_pickpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='link',
            field=models.CharField(default='http://localhost:8000/main/groupdiary/all', max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(),
        ),
    ]
