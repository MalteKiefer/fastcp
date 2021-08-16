# Generated by Django 3.2.6 on 2021-08-13 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_file_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=models.CharField(blank=True, choices=[('file', 'File'), ('directory', 'Directory')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
