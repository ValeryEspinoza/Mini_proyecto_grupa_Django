# Generated by Django 5.1.2 on 2024-10-25 17:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id_access', models.AutoField(primary_key=True, serialize=False)),
                ('access_name', models.CharField(max_length=100)),
                ('permissions', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id_area', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=100)),
                ('area_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id_category', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id_client', models.AutoField(primary_key=True, serialize=False)),
                ('client_name', models.CharField(max_length=100)),
                ('client_lastname', models.CharField(max_length=100)),
                ('client_email', models.CharField(max_length=200)),
                ('register_Date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Method',
            fields=[
                ('id_payment_method', models.AutoField(primary_key=True, serialize=False)),
                ('payment_method', models.CharField(max_length=100)),
                ('payment_method_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sell_Type',
            fields=[
                ('id_sell_type', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=100)),
                ('type_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('id_sub_category', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=100)),
                ('sub_category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Supplier_Categories',
            fields=[
                ('id_supplier_category', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_category_name', models.CharField(max_length=100)),
                ('supplier_category_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Clasification',
            fields=[
                ('id_employee_classification', models.AutoField(primary_key=True, serialize=False)),
                ('employee_clasifiaction_name', models.CharField(max_length=100)),
                ('id_access', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.access')),
                ('id_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.area')),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id_position', models.AutoField(primary_key=True, serialize=False)),
                ('position_name', models.CharField(max_length=100)),
                ('position_description', models.TextField()),
                ('id_employee_clasification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee_clasification')),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id_employee', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('age', models.IntegerField(choices=[(0, 'Under 18'), (1, '18-25'), (2, '26-35'), (3, 'Over 35')])),
                ('email', models.CharField(max_length=100)),
                ('iniciation_date', models.DateField()),
                ('id_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.position')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('product_description', models.TextField()),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.categories')),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id_inventory', models.AutoField(primary_key=True, serialize=False)),
                ('inventory_description', models.TextField()),
                ('stock', models.IntegerField()),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id_review', models.AutoField(primary_key=True, serialize=False)),
                ('review', models.TextField()),
                ('calification', models.DecimalField(decimal_places=1, max_digits=2)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
            ],
        ),
        migrations.CreateModel(
            name='sell_detail',
            fields=[
                ('id_sell_detail', models.AutoField(primary_key=True, serialize=False)),
                ('sell_date', models.DateField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxes', models.DecimalField(decimal_places=2, max_digits=8)),
                ('total', models.DecimalField(decimal_places=2, max_digits=8)),
                ('id_paymenth_method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.payment_method')),
                ('id_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id_record', models.AutoField(primary_key=True, serialize=False)),
                ('id_sell_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sell_detail')),
            ],
        ),
        migrations.AddField(
            model_name='payment_method',
            name='id_sell_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sell_type'),
        ),
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('id_sell', models.AutoField(primary_key=True, serialize=False)),
                ('id_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients')),
            ],
        ),
        migrations.AddField(
            model_name='sell_detail',
            name='id_sell',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sells'),
        ),
        migrations.AddField(
            model_name='categories',
            name='id_sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.sub_categories'),
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id_supplier', models.AutoField(primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(max_length=100)),
                ('supplier_description', models.TextField()),
                ('id_supplier_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.supplier_categories')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='id_suplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.suppliers'),
        ),
    ]
