from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings

class Medicine(models.Model):
    class Presentation(models.TextChoices):
        TABLET = "TAB", "Tableta / Comprimido"
        CAPSULE = "CAP", "Cápsula"
        SYRUP = "SYR", "Jarabe / Solución"
        INJECTION = "INJ", "Inyectable"
        CREAM = "CRM", "Crema / Pomada"
        DROPS = "DRP", "Gotas"
        INHALER = "INH", "Inhalador"
        OTHER = "OTH", "Otro"

    # Información básica
    name = models.CharField(
        max_length=150,
        verbose_name="Nombre comercial",
        help_text="Ej: Paracetamol Genfar, Ibuprofeno BSN",
    )
    
    generic_name = models.CharField(
        max_length=150,
        blank=True,
        verbose_name="Nombre genérico",
        help_text="Ej: Paracetamol, Ibuprofeno",
    )    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="medicines",
        verbose_name="Usuario / Paciente",
    )
    brand_or_laboratory = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Laboratorio / Marca",
    )

    # Composición y forma
    concentration = models.CharField(
        max_length=50,
        help_text="Ej: 500 mg, 10 mg/ml, 5%",
        verbose_name="Concentración",
    )
    presentation = models.CharField(
        max_length=3,
        choices=Presentation.choices,
        default=Presentation.TABLET,
        verbose_name="Presentación",
    )

    # Detalles médicos adicionales
    description = models.TextField(
        blank=True,
        verbose_name="Descripción / Indicaciones",
    )
    contraindications = models.TextField(
        blank=True,
        verbose_name="Contraindicaciones",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de creación",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Última actualización",
    )

    class Meta:
        verbose_name = "Medicamento"
        verbose_name_plural = "Medicamentos"
        ordering = ["name"]
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"{self.name} - {self.concentration}"