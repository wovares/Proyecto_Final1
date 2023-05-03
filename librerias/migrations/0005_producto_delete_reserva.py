# Generated by Django 4.1.6 on 2023-04-26 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("librerias", "0004_reserva"),
    ]

    operations = [
        migrations.CreateModel(
            name="Producto",
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
                ("nombre", models.CharField(max_length=100)),
                ("apellido", models.CharField(max_length=100)),
                ("correo", models.EmailField(max_length=254)),
                (
                    "fecha_creacion",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.DeleteModel(
            name="Reserva",
        ),
    ]