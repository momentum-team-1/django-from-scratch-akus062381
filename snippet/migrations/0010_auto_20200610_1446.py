# Generated by Django 3.0.6 on 2020-06-10 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippet', '0009_auto_20200608_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('HTML', 'HTML'), ('CSS', 'CSS'), ('JAVASCRIPT', 'JavaScript'), ('PYTHON', 'Python')], default='', max_length=255),
        ),
    ]
