# Generated by Django 3.2.18 on 2023-04-08 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_metadata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inbodyimage',
            old_name='result',
            new_name='inbody_score',
        ),
        migrations.AddField(
            model_name='inbodyimage',
            name='waist_hip_ratio',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
