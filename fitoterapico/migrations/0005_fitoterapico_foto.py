# Generated by Django 5.1.6 on 2025-03-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitoterapico', '0004_rename_name_tipo_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='fitoterapico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fitoterapico/'),
        ),
    ]
