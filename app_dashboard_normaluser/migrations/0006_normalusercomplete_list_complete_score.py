# Generated by Django 3.2.6 on 2022-02-16 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_dashboard_normaluser', '0005_normalusercomplete_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalusercomplete_list',
            name='complete_score',
            field=models.IntegerField(default=0),
        ),
    ]
