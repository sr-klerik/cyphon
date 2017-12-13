# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-12 19:10
from __future__ import unicode_literals

from django.db import migrations


def populate_names(apps, schema_editor):
    """Populate names for Distilleries that don't have one."""
    Distillery = apps.get_model('distilleries', 'Distillery')
    for distillery in Distillery.objects.filter(name__isnull=True):
        collection = distillery.collection
        warehouse = collection.warehouse
        distillery.name = '%s.%s.%s' % (warehouse.backend, warehouse.name,
                                        collection.name)
        distillery.name = 'test'
        distillery.save()


class Migration(migrations.Migration):

    dependencies = [
        ('distilleries', '0002_add_name_field'),
    ]

    operations = [
        migrations.RunPython(populate_names),
    ]
