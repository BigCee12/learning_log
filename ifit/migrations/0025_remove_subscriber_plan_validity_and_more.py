# Generated by Django 4.0.6 on 2023-01-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifit', '0024_alter_subscription_options_alter_subscription_plan_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriber',
            name='plan_validity',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='subscription_plan',
        ),
        migrations.AddField(
            model_name='subscriber',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='mobile_no',
            field=models.CharField(max_length=20, null=True),
        ),
    ]