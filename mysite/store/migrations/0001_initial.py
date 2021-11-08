# Generated by Django 3.2.8 on 2021-11-02 17:08

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment_number', models.CharField(blank=True, default='', max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('default', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 231567, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 231583, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 234757, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 234775, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown offer', max_length=255)),
                ('description', models.TextField(default='Unknown description')),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 232736, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 232751, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('delivery_fee', models.FloatField(default=0.0)),
                ('average_rating', models.DecimalField(decimal_places=1, default=0.0, max_digits=9)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('available', models.BooleanField(default=True)),
                ('minimum_stock', models.IntegerField(default=10)),
                ('stock', models.IntegerField(default=0)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233114, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233128, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
                ('offer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.offer')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('username', models.CharField(default=None, max_length=255)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('level', models.IntegerField(default=1)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 231226, tzinfo=utc))),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 231245, tzinfo=utc))),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('postcode', models.CharField(blank=True, max_length=10)),
                ('phone', models.CharField(blank=True, max_length=14)),
                ('assistance_email', models.EmailField(max_length=254, null=True)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 232376, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 232391, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('evaluation', models.DecimalField(blank=True, decimal_places=2, max_digits=9)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 234313, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 234328, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233557, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233572, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stripe_charge_id', models.CharField(max_length=50)),
                ('amount', models.FloatField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 236537, tzinfo=utc))),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 236553, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 236564, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='Orderproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('being_delivered', models.BooleanField(default=False)),
                ('received', models.BooleanField(default=False)),
                ('refund_requested', models.BooleanField(default=False)),
                ('refund_granted', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 235530, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 235547, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('billing_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='store.address')),
                ('coupon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.coupon')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.payment')),
                ('products', models.ManyToManyField(to='store.Orderproduct')),
                ('shipping_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shipping_address', to='store.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
        migrations.CreateModel(
            name='LoyalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('points', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233921, tzinfo=utc), null=True)),
                ('updated_at', models.DateField(default=datetime.datetime(2021, 11, 2, 17, 8, 47, 233935, tzinfo=utc), null=True)),
                ('deleted_at', models.DateField(blank=True, default=None, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.user')),
            ],
        ),
    ]
