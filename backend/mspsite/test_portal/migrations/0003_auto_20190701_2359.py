# Generated by Django 2.2.2 on 2019-07-01 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_portal', '0002_auto_20190701_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
