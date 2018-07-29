# Generated by Django 2.0.6 on 2018-07-29 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Automated_call',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recording_url', models.CharField(max_length=400)),
                ('call_time', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.CharField(choices=[('OP', 'On progress'), ('RE', 'Resolved')], default='OP', max_length=2),
        ),
    ]
