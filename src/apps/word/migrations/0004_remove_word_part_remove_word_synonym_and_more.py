# Generated by Django 5.0.4 on 2024-05-15 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0003_alter_userword_unique_together'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='part',
        ),
        migrations.RemoveField(
            model_name='word',
            name='synonym',
        ),
        migrations.RemoveField(
            model_name='word',
            name='translation',
        ),
        migrations.AddField(
            model_name='word',
            name='part_of_speech',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_words', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userword',
            name='word',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_users', to='word.word'),
        ),
        migrations.AlterField(
            model_name='word',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='word',
            name='transcription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('part_of_speech', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('frequency', models.IntegerField(null=True)),
                ('word', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='word.word')),
            ],
        ),
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('part_of_speech', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=1, null=True)),
                ('frequency', models.IntegerField(null=True)),
                ('translation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='synonyms', to='word.translation')),
            ],
        ),
        migrations.CreateModel(
            name='Meaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('translation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meanings', to='word.translation')),
            ],
        ),
    ]
