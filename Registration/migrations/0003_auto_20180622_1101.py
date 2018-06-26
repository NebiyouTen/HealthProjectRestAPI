# Generated by Django 2.0.6 on 2018-06-22 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20180621_1026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_type', models.CharField(choices=[('SX', 'Sexual Violence'), ('EC', 'Economic'), ('EM', 'Emotional'), ('PY', 'Physical'), ('OT', 'Other')], max_length=2)),
                ('note', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='clinet',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='clinet',
            name='estimated_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='detail',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.Clinet'),
        ),
    ]
