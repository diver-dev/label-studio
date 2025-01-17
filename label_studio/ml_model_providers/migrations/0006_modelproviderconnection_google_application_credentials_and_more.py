# Generated by Django 5.1.4 on 2025-01-03 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "ml_model_providers",
            "0005_modelproviderconnection_budget_alert_threshold_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="modelproviderconnection",
            name="google_application_credentials",
            field=models.TextField(
                blank=True,
                help_text="The content of GOOGLE_APPLICATION_CREDENTIALS json file",
                null=True,
                verbose_name="google application credentials",
            ),
        ),
        migrations.AddField(
            model_name="modelproviderconnection",
            name="google_location",
            field=models.CharField(
                blank=True,
                help_text="Google project location",
                max_length=255,
                null=True,
                verbose_name="google location",
            ),
        ),
        migrations.AddField(
            model_name="modelproviderconnection",
            name="google_project_id",
            field=models.CharField(
                blank=True,
                help_text="Google project ID",
                max_length=255,
                null=True,
                verbose_name="google project id",
            ),
        ),
        migrations.AlterField(
            model_name="modelproviderconnection",
            name="provider",
            field=models.CharField(
                choices=[
                    ("OpenAI", "OpenAI"),
                    ("AzureOpenAI", "AzureOpenAI"),
                    ("VertexAI", "VertexAI"),
                    ("Custom", "Custom"),
                ],
                default="OpenAI",
                max_length=255,
            ),
        ),
    ]
