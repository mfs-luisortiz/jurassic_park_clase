# Generated by Django 2.2.6 on 2019-11-26 04:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dinosaurios', '0008_auto_20191126_0415'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Votacion',
            new_name='VotacionDino',
        ),
    ]
