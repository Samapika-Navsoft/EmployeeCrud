# Generated by Django 4.0.6 on 2022-07-15 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0003_rename_empolyee_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='media/pictures'),
        ),
    ]