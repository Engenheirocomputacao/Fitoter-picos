# Generated by Django 5.1.6 on 2025-03-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitoterapico', '0006_fitoterapicoinventario'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitoterapico',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
