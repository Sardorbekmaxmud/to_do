# Generated by Django 4.2.2 on 2023-06-19 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=250)),
                ('status', models.BooleanField()),
                ('created_at', models.DateTimeField(default=None)),
                ('update_at', models.DateTimeField(default=None)),
            ],
            options={
                'db_table': 'to_do_list',
            },
        ),
    ]