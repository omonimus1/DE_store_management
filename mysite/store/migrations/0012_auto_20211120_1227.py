# Generated by Django 3.2.8 on 2021-11-20 12:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20211120_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 167796, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 170781, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 169981, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 168556, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 171526, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 172507, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 172492, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 168901, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productdiscounted',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 169289, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 169649, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 170359, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 12, 27, 56, 167465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(default=1),
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]