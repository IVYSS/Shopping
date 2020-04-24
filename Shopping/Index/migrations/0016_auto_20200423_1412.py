# Generated by Django 3.0.3 on 2020-04-23 07:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0008_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Index', '0015_auto_20200423_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ordered', models.BooleanField(default=False)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Index.Product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Order_product',
        ),
    ]
