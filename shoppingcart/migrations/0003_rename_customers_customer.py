# Generated by Django 3.2.4 on 2021-06-05 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoppingcart', '0002_auto_20210604_2153'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
    ]
