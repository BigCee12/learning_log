# Generated by Django 4.0.6 on 2022-08-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifit', '0007_remove_subscriptionplan_highlight_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customclient',
            name='last_login',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
