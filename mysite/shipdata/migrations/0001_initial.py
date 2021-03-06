# Generated by Django 3.2.6 on 2021-08-29 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('power', models.FloatField()),
                ('sensorRange', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Fuel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('capacity', models.FloatField()),
                ('power', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Hull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('passiveHeat', models.FloatField()),
                ('activeHeat', models.FloatField()),
                ('hp', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HyperDrive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('mean', models.FloatField()),
                ('stdev', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='LifeSupport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('o2Capacity', models.FloatField()),
                ('power', models.FloatField()),
                ('co2reprocesing', models.FloatField()),
                ('tempcontrol', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PowerBank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('mean', models.FloatField()),
                ('stdev', models.FloatField()),
                ('capacity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reactor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('mean', models.FloatField()),
                ('stdev', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Repulsion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('strength', models.IntegerField()),
                ('charge', models.FloatField()),
                ('disRate', models.FloatField()),
                ('chRate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Thruster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('size', models.IntegerField()),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('mean', models.FloatField()),
                ('stdev', models.FloatField()),
                ('power', models.FloatField()),
                ('overload', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('repairness', models.IntegerField()),
                ('maxTemp', models.IntegerField()),
                ('minTemp', models.IntegerField()),
                ('damageK', models.FloatField()),
                ('damageH', models.FloatField()),
                ('damageE', models.FloatField()),
                ('power', models.FloatField()),
                ('ammoType', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designer', models.CharField(max_length=100)),
                ('shipType', models.CharField(max_length=100)),
                ('locSystem', models.CharField(max_length=100)),
                ('locX', models.FloatField()),
                ('locY', models.FloatField()),
                ('locZ', models.FloatField()),
                ('computers', models.ManyToManyField(to='shipdata.Computer')),
                ('fuels', models.ManyToManyField(to='shipdata.Fuel')),
                ('hulls', models.ManyToManyField(to='shipdata.Hull')),
                ('hyperDrives', models.ManyToManyField(to='shipdata.HyperDrive')),
                ('lifeSupports', models.ManyToManyField(to='shipdata.LifeSupport')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.player')),
                ('powerBanks', models.ManyToManyField(to='shipdata.PowerBank')),
                ('reactors', models.ManyToManyField(to='shipdata.Reactor')),
                ('repulsions', models.ManyToManyField(to='shipdata.Repulsion')),
                ('thrusters', models.ManyToManyField(to='shipdata.Thruster')),
                ('weapons', models.ManyToManyField(to='shipdata.Weapon')),
            ],
        ),
    ]
