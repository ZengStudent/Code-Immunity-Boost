# Generated by Django 3.2.6 on 2022-01-13 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_contract', '0007_contract_contract_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contract_content',
            old_name='content_present',
            new_name='content_precent',
        ),
        migrations.RenameField(
            model_name='contract_perfect',
            old_name='perfect_present',
            new_name='perfect_precent',
        ),
    ]