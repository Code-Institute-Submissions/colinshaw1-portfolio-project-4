# Generated by Django 4.1.1 on 2022-09-12 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_contact_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
