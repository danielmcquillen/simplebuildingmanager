from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel

from simplebuildingmanager.buildings.models import Building


class BaseRecord(TimeStampedModel):
    date = models.DateField(help_text=_("Use the first day of the month for monthly records"))
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__} for {self.building.name} on {self.date}"


class EnergyRecord(BaseRecord):
    class Meta:
        indexes = [
            models.Index(fields=["building"]),
            models.Index(fields=["date"]),
        ]
        ordering = ["date"]
        unique_together = ("building", "date")
        verbose_name = _("Energy Record")

    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="energy_records",
    )

    kwh = models.FloatField(help_text=_("Energy used during this period in kilowatt-hours"))
    source = models.CharField(
        max_length=100,
        blank=True,
        help_text=_("e.g., electricity, gas, solar"),
    )


class WaterRecord(BaseRecord):
    class Meta:
        indexes = [
            models.Index(fields=["building"]),
            models.Index(fields=["date"]),
        ]
        ordering = ["date"]
        unique_together = ("building", "date")
        verbose_name = _("Water Record")

    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="water_records",
    )

    cubic_meters = models.FloatField(help_text=_("Water used during this period in cubic meters"))
    source = models.CharField(
        max_length=100,
        blank=True,
        help_text=_("e.g., municipal, rainwater"),
    )


class CostRecord(BaseRecord):
    class Meta:
        indexes = [
            models.Index(fields=["building"]),
            models.Index(fields=["date"]),
        ]
        ordering = ["date"]
        unique_together = ("building", "date")
        verbose_name = _("Cost Record")

    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="cost_records",
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text=_("Cost in dollars"),
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        help_text=_("e.g., electricity, maintenance, gas"),
    )


class EmissionRecord(BaseRecord):
    class Meta:
        indexes = [
            models.Index(fields=["building"]),
            models.Index(fields=["date"]),
        ]
        ordering = ["date"]
        unique_together = ("building", "date")
        verbose_name = _("Emission Record")

    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name="emission_records",
    )

    kg_co2e = models.FloatField(help_text=_("Estimated or measured emissions in kilograms of CO₂e"))
    method = models.CharField(
        max_length=100,
        blank=True,
        help_text=_("e.g., calculated, metered, offset"),
    )
