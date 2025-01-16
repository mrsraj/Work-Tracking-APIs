# Generated by Django 5.1.4 on 2025-01-15 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wtapp', '0004_task_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='board',
        ),
        migrations.RemoveField(
            model_name='card',
            name='category',
        ),
        migrations.RemoveField(
            model_name='card',
            name='user',
        ),
        migrations.RemoveField(
            model_name='cardcategory',
            name='board',
        ),
        migrations.RemoveField(
            model_name='cardcategory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='board',
            name='modification_timestamp',
        ),
        migrations.RemoveField(
            model_name='board',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='BoardMember',
        ),
        migrations.DeleteModel(
            name='Card',
        ),
        migrations.DeleteModel(
            name='CardCategory',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]