# Generated by Django 3.0.7 on 2020-06-16 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flashcards', '0006_auto_20200616_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learn',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='level',
            field=models.ForeignKey(default='HSK1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='flashcards.Level'),
        ),
    ]
