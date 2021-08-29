# Generated by Django 3.2.6 on 2021-08-29 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solapi', '0003_auto_20210829_0351'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='system',
            name='orbit',
        ),
        migrations.AddField(
            model_name='system',
            name='locX',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system',
            name='locY',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='system',
            name='locZ',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
