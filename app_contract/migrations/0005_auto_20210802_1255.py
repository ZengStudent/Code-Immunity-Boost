# Generated by Django 3.2.5 on 2021-08-02 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_contract', '0004_auto_20210802_1010'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract_completedtable',
            name='complete_isadvance',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contract_completedtable',
            name='complete_isbasic',
            field=models.BooleanField(default=False),
        ),
    ]
