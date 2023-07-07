# Generated by Django 3.2.20 on 2023-07-07 04:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('to_do', '0003_alter_todolistmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolistmodel',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
