# Generated by Django 3.0.7 on 2020-06-15 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0003_auto_20200615_0052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='learn',
            options={'verbose_name': 'Learn', 'verbose_name_plural': 'Learned Words'},
        ),
        migrations.AddField(
            model_name='learn',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learn',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
