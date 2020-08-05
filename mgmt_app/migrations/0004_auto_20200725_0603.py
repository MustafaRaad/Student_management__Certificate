# Generated by Django 3.0.8 on 2020-07-25 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgmt_app', '0003_auto_20200722_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='AR_college',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='student',
            name='AR_department',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='student',
            name='AR_full_name',
            field=models.CharField(default='مصطفى رعد مطشر', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='final_grade',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
