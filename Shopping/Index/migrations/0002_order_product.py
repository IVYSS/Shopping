# Generated by Django 3.0.3 on 2020-04-20 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0001_initial'),
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('order_no', models.IntegerField(primary_key=True, serialize=False)),
                ('unit', models.IntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Product')),
            ],
        ),
    ]
