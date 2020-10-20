# Generated by Django 3.0.5 on 2020-10-19 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_name', models.CharField(default='', max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(default='', max_length=70)),
                ('destination', models.CharField(default='', max_length=70)),
                ('distance', models.IntegerField(default=0)),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='routes', to='deliveries.Delivery')),
            ],
        ),
    ]
