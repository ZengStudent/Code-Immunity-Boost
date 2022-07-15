# Generated by Django 3.2.6 on 2022-02-14 00:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app_contract', '0009_auto_20220208_1341'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_dashboard_normaluser', '0004_auto_20211111_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='normalusercomplete_list',
            fields=[
                ('id', models.PositiveIntegerField(default=1, primary_key=True, serialize=False)),
                ('editorcode_completedtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('editorcode_isbasic', models.BooleanField(default=False)),
                ('editorcode_isadvance', models.BooleanField(default=False)),
                ('author', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contract_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_contract.contractinstance')),
            ],
        ),
    ]
