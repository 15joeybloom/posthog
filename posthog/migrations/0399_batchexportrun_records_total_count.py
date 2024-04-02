# Generated by Django 4.1.13 on 2024-03-25 14:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0398_alter_externaldatasource_source_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="batchexportrun",
            name="records_total_count",
            field=models.IntegerField(
                help_text="The total count of records that should be exported in this BatchExportRun.", null=True
            ),
        ),
    ]