# Generated by Django 4.2.7 on 2024-03-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_products_prod_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='TAGS',
            field=models.ManyToManyField(blank=True, to='accounts.tag'),
        ),
    ]
