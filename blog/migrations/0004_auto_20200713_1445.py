# Generated by Django 3.0.7 on 2020-07-13 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200713_1431'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='l1',
            field=models.CharField(default='Tester', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='l2',
            field=models.CharField(default='tester', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='l3',
            field=models.CharField(default='tester1', max_length=100),
            preserve_default=False,
        ),
    ]
