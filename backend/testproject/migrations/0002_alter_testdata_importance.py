# Generated by Django 3.2 on 2022-02-14 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testdata',
            name='importance',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]