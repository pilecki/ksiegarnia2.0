# Generated by Django 3.0.9 on 2020-08-25 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200825_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description1',
            field=models.CharField(blank=True, max_length=370, null=True),
        ),
    ]
