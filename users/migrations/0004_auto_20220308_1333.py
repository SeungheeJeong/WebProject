# Generated by Django 2.2.5 on 2022-03-08 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_hp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='hp',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
