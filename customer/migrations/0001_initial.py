# Generated by Django 4.1.4 on 2022-12-16 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=250)),
                ('lastname', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='CustomerData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('phone_num', models.IntegerField(max_length=10)),
                ('card_num', models.IntegerField(max_length=12)),
                ('customers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customers')),
            ],
        ),
    ]
