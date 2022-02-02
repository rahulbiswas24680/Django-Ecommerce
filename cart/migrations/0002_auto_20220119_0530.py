# Generated by Django 3.2.9 on 2022-01-19 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='order',
            name='pin',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(default='', max_length=25),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
