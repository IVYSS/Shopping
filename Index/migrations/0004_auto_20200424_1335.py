# Generated by Django 3.0.3 on 2020-04-24 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_remove_product_type_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='payment_option',
            field=models.CharField(choices=[('S', 'Stripe'), ('P', 'PayPal')], default=None, max_length=1, null=True),
        ),
    ]
