# Generated by Django 3.2.5 on 2021-08-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dashboard_normaluser', '0002_auto_20210802_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='normalusercompletecode',
            name='editorcode_isbasic',
            field=models.BooleanField(default=False),
        ),
    ]
