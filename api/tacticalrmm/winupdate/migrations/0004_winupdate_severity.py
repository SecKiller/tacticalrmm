# Generated by Django 2.2.7 on 2019-12-02 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winupdate', '0003_auto_20191201_0426'),
    ]

    operations = [
        migrations.AddField(
            model_name='winupdate',
            name='severity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]