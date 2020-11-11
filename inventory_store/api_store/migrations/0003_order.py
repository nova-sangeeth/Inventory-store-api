# Generated by Django 3.1.3 on 2020-11-11 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_store', '0002_batch'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField()),
                ('units', models.IntegerField()),
                ('company', models.CharField(max_length=128)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_store.batch')),
            ],
        ),
    ]