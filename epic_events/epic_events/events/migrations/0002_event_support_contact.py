# Generated by Django 3.2.8 on 2021-11-04 08:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='support_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='event_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]
