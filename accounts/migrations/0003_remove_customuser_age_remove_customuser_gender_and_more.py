# Generated by Django 4.2.16 on 2025-01-03 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='height',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='weight',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]