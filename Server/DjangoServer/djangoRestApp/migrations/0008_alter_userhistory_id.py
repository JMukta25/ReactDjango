# Generated by Django 4.0.3 on 2022-12-30 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoRestApp', '0007_userhistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='id',
            field=models.IntegerField(max_length=100000000, primary_key=True, serialize=False),
        ),
    ]
