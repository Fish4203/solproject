# Generated by Django 3.2.6 on 2021-08-30 03:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210830_0256'),
    ]

    operations = [
        migrations.CreateModel(
            name='FactionFaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rep', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='users.faction')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target', to='users.faction')),
            ],
        ),
        migrations.AddField(
            model_name='faction',
            name='factions',
            field=models.ManyToManyField(through='users.FactionFaction', to='users.Faction'),
        ),
    ]
