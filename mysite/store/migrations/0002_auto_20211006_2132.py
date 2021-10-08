# Generated by Django 3.2.8 on 2021-10-06 20:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=255)),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('average_rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=9)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('stock_available', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 383403, tzinfo=utc), null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offer')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 335404, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='deleted_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 335404, tzinfo=utc), null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='postcode',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='updated_at',
            field=models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 335404, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('evaluation', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='LoyalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(default=datetime.datetime(2021, 10, 6, 20, 32, 5, 384403, tzinfo=utc), null=True)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
    ]
