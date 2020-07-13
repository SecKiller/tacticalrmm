# Generated by Django 3.0.7 on 2020-06-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_coresettings_mesh_token"),
    ]

    operations = [
        migrations.AddField(
            model_name="coresettings",
            name="mesh_site",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="coresettings",
            name="mesh_username",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="coresettings",
            name="mesh_token",
            field=models.CharField(blank=True, default="", max_length=255, null=True),
        ),
    ]