# Generated by Django 3.0.6 on 2020-05-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_myblog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblog',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]