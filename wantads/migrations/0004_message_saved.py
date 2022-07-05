# Generated by Django 3.2.14 on 2022-07-05 12:12

import django.db.models.deletion
import django_jalali.db.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("wantads", "0003_auto_20220705_0154"),
    ]

    operations = [
        migrations.CreateModel(
            name="Saved",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ("updated", django_jalali.db.models.jDateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wantads_saved",
                        related_query_name="wantads_saved",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "want",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wantads_saved",
                        related_query_name="wantads_saved",
                        to="wantads.wantad",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", django_jalali.db.models.jDateTimeField(auto_now_add=True)),
                ("updated", django_jalali.db.models.jDateTimeField(auto_now=True)),
                ("text", models.TextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wantads_message",
                        related_query_name="wantads_message",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "want",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="wantads_message",
                        related_query_name="wantads_message",
                        to="wantads.wantad",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]