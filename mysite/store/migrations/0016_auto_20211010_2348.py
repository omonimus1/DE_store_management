# Generated by Django 3.2.8 on 2021-10-10 23:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_auto_20211010_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 499641, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 499659, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 501299, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 501313, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 499950, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='deleted_at',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 499964, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 504762, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 500322, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 500336, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 500936, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 500953, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 501702, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 501716, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 476164, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 10, 23, 48, 36, 476195, tzinfo=utc), null=True),
        ),
    ]
