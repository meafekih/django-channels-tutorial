# Generated by Django 4.2.4 on 2023-08-17 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='conversation',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
    ]
