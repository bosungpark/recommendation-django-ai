# Generated by Django 3.2 on 2022-02-10 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0005_testdata_impressions_cnt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='impressions_cnt',
            field=models.IntegerField(default=0),
        ),
    ]
