# Generated by Django 4.0.3 on 2022-07-14 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empolyee',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
