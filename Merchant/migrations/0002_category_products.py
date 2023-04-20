# Generated by Django 4.2 on 2023-04-19 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Merchant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'categories',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.FloatField(max_length=20)),
                ('discount', models.IntegerField()),
                ('image', models.FileField(upload_to='products/')),
                ('Merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Merchant.merchant')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Merchant.category')),
            ],
            options={
                'verbose_name_plural': 'products',
                'db_table': 'products',
            },
        ),
    ]
