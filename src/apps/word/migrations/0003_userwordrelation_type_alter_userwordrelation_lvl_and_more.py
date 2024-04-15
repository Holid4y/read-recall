# Generated by Django 5.0.4 on 2024-04-15 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_userwordrelation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwordrelation',
            name='type',
            field=models.CharField(choices=[('RC', 'recognize'), ('RP', 'reproduction ')], default='RC', max_length=2, verbose_name='training type'),
        ),
        migrations.AlterField(
            model_name='userwordrelation',
            name='lvl',
            field=models.IntegerField(default=1, verbose_name='lvl'),
        ),
        migrations.AlterField(
            model_name='userwordrelation',
            name='time',
            field=models.IntegerField(verbose_name='time'),
        ),
    ]
