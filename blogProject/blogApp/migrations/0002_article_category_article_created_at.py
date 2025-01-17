# Generated by Django 5.0.3 on 2024-04-04 00:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('취미', '취미'), ('음식', '음식'), ('프로그래밍', '프로그래밍')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
