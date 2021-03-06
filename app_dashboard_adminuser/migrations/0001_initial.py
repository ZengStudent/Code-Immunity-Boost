# Generated by Django 3.2.5 on 2021-08-02 01:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='adminuser',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('can_use_admin', 'Can Use Admin'),),
            },
        ),
    ]
