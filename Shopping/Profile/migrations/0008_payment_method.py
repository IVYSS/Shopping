# Generated by Django 3.0.3 on 2020-04-25 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0007_auto_20200425_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'PayPal')], default='S', max_length=10),
            preserve_default=False,
        ),
    ]
