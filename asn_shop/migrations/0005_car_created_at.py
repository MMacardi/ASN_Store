# Generated by Django 5.2.1 on 2025-05-12 13:25

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asn_shop', '0004_myuser_groups_myuser_user_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
