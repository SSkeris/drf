# Generated by Django 4.2.2 on 2024-06-23 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_alter_lesson_course"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
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
                (
                    "date_of_payment",
                    models.DateTimeField(
                        auto_now_add=True, null=True, verbose_name="дата оплаты"
                    ),
                ),
                (
                    "payment_amount",
                    models.PositiveIntegerField(
                        blank=True,
                        help_text="введите сумму оплаты",
                        null=True,
                        verbose_name="сумма оплаты",
                    ),
                ),
                (
                    "payment_method",
                    models.CharField(
                        choices=[("Cash", "Наличные"), ("Non-cash", "Безнал")],
                        help_text="выберите способ оплаты",
                        max_length=20,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "paid_course",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.course",
                        verbose_name="оплаченный курс",
                    ),
                ),
                (
                    "paid_lesson",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="materials.lesson",
                        verbose_name="оплаченный урок",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        help_text="выберите пользователя",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_payment",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
            },
        ),
    ]