# Generated by Django 2.1.7 on 2019-02-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Circolari', '0003_auto_20190223_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='circolare',
            name='Allegato',
            field=models.URLField(blank=True, null=True),
        ),
    ]
