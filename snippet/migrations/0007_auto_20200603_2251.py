# Generated by Django 3.0.6 on 2020-06-04 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0006_auto_20200603_2249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='snippet',
            new_name='user',
        ),
    ]
