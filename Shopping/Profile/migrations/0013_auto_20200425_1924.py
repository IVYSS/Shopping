# Generated by Django 3.0.3 on 2020-04-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0012_auto_20200425_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
