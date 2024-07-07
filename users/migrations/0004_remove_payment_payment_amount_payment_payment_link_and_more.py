# Generated by Django 4.2.2 on 2024-07-06 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_remove_user_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="payment_amount",
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="payment_status",
            field=models.CharField(
                blank=True, max_length=30, null=True, verbose_name="статус платежа"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="id сессии"
            ),
        ),
    ]