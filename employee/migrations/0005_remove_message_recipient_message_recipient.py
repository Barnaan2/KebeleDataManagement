# Generated by Django 4.1.2 on 2023-01-13 01:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_remove_message_recipient_message_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='recipient',
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='employee.employee'),
        ),
    ]