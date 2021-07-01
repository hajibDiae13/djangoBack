# Generated by Django 3.2.5 on 2021-07-01 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcommerceBase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('inStock', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('sold', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('label', models.CharField(max_length=200)),
            ],
        ),
    ]
