# Generated by Django 3.0.3 on 2020-04-19 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='My_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('A', 'available'), ('U', 'unavailable')], max_length=1)),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('upload', models.ImageField(blank=True, null=True, upload_to='')),
                ('method', models.CharField(choices=[('paypal', 'paypal'), ('creditcard', 'creditcard'), ('truewallet', 'truewallet')], max_length=10)),
                ('financial_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.My_User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('delivery_place', models.TextField(blank=True, null=True)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.CharField(choices=[('NS', 'Notyetshipped'), ('S', 'Shipping'), ('D', 'Delivered')], max_length=2)),
                ('customer_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.My_User')),
                ('promotion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.Promotion')),
            ],
        ),
        migrations.CreateModel(
            name='Financial_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date', models.DateField()),
                ('financial_type', models.CharField(choices=[('revenue', 'revenue'), ('expense', 'expense')], max_length=8)),
                ('financial_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Profile.My_User')),
            ],
        ),
    ]
