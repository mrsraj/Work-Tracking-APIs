# Generated by Django 5.0.2 on 2025-02-01 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtapp', '0009_boardmember_added_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
