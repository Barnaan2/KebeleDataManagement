# Generated by Django 4.1.2 on 2023-01-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kebele', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'ordering': ['resident']},
        ),
        migrations.AlterModelOptions(
            name='resident',
            options={'ordering': ['first_name']},
        ),
        migrations.AddField(
            model_name='address',
            name='hnum',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
