# Generated by Django 3.0.9 on 2020-08-25 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='comingsoon',
            options={'verbose_name_plural': 'Comming Soon'},
        ),
        migrations.AlterModelOptions(
            name='formats',
            options={'verbose_name_plural': 'Formats'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='description2',
        ),
        migrations.AddField(
            model_name='product',
            name='description1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
