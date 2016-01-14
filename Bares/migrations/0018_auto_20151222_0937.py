# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bares', '0017_auto_20151222_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='logo',
            field=models.ImageField(upload_to=b'media', blank=True),
        ),
    ]
