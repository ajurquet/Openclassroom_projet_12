# Generated by Django 3.2.8 on 2021-11-06 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contracts', '0002_contract_sales_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='sales_contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='contract_assigned_to', to=settings.AUTH_USER_MODEL),
        ),
    ]