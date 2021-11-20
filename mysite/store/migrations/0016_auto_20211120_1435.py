# Generated by Django 3.2.8 on 2021-11-20 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20211120_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='lat',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='address',
            name='long',
            field=models.FloatField(default=0.0),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 52078, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 55817, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 54847, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 53112, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 56707, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 57905, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 57887, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 53531, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productdiscounted',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 54007, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 54440, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 55296, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 14, 35, 59, 51684, tzinfo=utc)),
        ),
    ]