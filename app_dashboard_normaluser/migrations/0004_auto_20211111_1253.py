# Generated by Django 3.2.6 on 2021-11-11 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_dashboard_normaluser', '0003_alter_normalusercompletecode_editorcode_isbasic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normaluser',
            name='correct_counts',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='mistake_counts',
        ),
    ]
