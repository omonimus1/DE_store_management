# Generated by Django 3.2.8 on 2021-11-18 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20211118_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 572854, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 576199, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 575262, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 574105, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 576935, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 577943, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 577928, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 574461, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='minimum_stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 574880, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 575627, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 573700, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 18, 15, 2, 7, 572535, tzinfo=utc)),
        ),
    ]
