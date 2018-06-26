# Generated by Django 2.0.6 on 2018-06-26 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0005_auto_20180622_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('is_owner', models.BooleanField()),
                ('purpose', models.CharField(max_length=400)),
                ('time', models.DateTimeField()),
                ('case_type', models.CharField(choices=[('SX', 'Sexual Violence'), ('EC', 'Economic'), ('EM', 'Emotional'), ('PY', 'Physical'), ('OT', 'Other')], max_length=2)),
                ('notes', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('date_of_birth', models.DateField(null=True)),
                ('estimated_age', models.IntegerField(null=True)),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Health_Center_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Health_Centers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Police_Station_service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Police_Stations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Safe_Spaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
                ('notes', models.CharField(max_length=400)),
                ('internal', models.BooleanField()),
                ('call', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Calls')),
                ('safe_space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Safe_Spaces')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='clinet',
            name='client_detail',
        ),
        migrations.DeleteModel(
            name='Clinet',
        ),
        migrations.DeleteModel(
            name='Clinet_Detail',
        ),
        migrations.AddField(
            model_name='service',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Staff'),
        ),
        migrations.AddField(
            model_name='police_station_service',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Service'),
        ),
        migrations.AddField(
            model_name='police_station_service',
            name='station',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Police_Stations'),
        ),
        migrations.AddField(
            model_name='health_center_service',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Health_Centers'),
        ),
        migrations.AddField(
            model_name='health_center_service',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Service'),
        ),
        migrations.AddField(
            model_name='calls',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Registration.Client'),
        ),
    ]
