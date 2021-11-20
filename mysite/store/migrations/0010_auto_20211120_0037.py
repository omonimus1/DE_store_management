# Generated by Django 3.2.8 on 2021-11-20 00:37

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20211119_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 74251, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 77956, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='loyalcard',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 77051, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 75438, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 78710, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 79760, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 79745, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 75798, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 76604, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 77511, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 75084, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 73931, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='ProductDiscounted',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 20, 0, 37, 41, 76211, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(blank=True, default=None, null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]
