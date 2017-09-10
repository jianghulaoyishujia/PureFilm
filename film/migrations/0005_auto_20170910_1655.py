# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_auto_20170910_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='by_link',
            field=models.CharField(max_length=2000, verbose_name='下载链接1', null=True),
        ),
    ]
