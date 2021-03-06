# Generated by Django 3.2.8 on 2021-11-02 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 692205, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 692239, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 695729, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 695744, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 694725, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 694738, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693552, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693566, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 696488, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 696505, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 697497, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 697482, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 697509, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693920, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693935, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 694359, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 694375, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 695289, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 695303, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693193, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 693208, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 691773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 58, 691791, tzinfo=utc)),
        ),
    ]
