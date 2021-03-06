# Generated by Django 2.2.3 on 2019-07-01 21:03

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190701_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyrecord',
            old_name='user_habit',
            new_name='owner_habit',
        ),
        migrations.RenameField(
            model_name='habit',
            old_name='user',
            new_name='owner',
        ),
        migrations.AddField(
            model_name='dailyrecord',
            name='num_achieved',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habit',
            name='date_started',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dailyrecord',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterUniqueTogether(
            name='dailyrecord',
            unique_together={('date', 'owner_habit')},
        ),
        migrations.RemoveField(
            model_name='dailyrecord',
            name='user',
        ),
    ]
