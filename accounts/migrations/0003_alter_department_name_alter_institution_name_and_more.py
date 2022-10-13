# Generated by Django 4.1.2 on 2022-10-10 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_department_institution_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
