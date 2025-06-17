from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from polymorphic.models import PolymorphicModel

from simplebuildingmanager.buildings.models import Building


class BaseRecord(PolymorphicModel, TimeStampedModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name="%(class)ss")
    date = models.DateField(help_text="Use the first day of the month for monthly records")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        class Meta:
            indexes = [
                models.Index(fields=["building"]),
                models.Index(fields=["date"]),
            ]
            abstract = True
            ordering = ["date"]
            unique_together = ("building", "date")

    def __str__(self):
        return f"{self.__class__.__name__} for {self.building.name} on {self.date}"


class EnergyRecord(BaseRecord):
    kwh = models.FloatField(help_text=_("Energy used during this period in kilowatt-hours"))
    source = models.CharField(max_length=100, blank=True, help_text="e.g., electricity, gas, solar")

    class Meta(BaseRecord.Meta):
        verbose_name = "Energy Record"


class WaterRecord(BaseRecord):
    cubic_meters = models.FloatField(help_text=_("Water used during this period in cubic meters"))
    source = models.CharField(max_length=100, blank=True, help_text="e.g., municipal, rainwater")

    class Meta(BaseRecord.Meta):
        verbose_name = "Water Record"


class CostRecord(BaseRecord):
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text=_("Cost in dollars"))
    category = models.CharField(max_length=100, blank=True, help_text=_("e.g., electricity, maintenance, gas"))

    class Meta(BaseRecord.Meta):
        verbose_name = "Cost Record"


class EmissionRecord(BaseRecord):
    kg_co2e = models.FloatField(help_text=_("Estimated or measured emissions in kilograms of CO₂e"))
    method = models.CharField(max_length=100, blank=True, help_text=_("e.g., calculated, metered, offset"))

    class Meta(BaseRecord.Meta):
        verbose_name = "Emission Record"
