from django.db import models

from simplebuildingmanager.buildings.constants import BuildingType


# Create your models here.
class Building(models.Model):
    name = models.CharField(max_length=500)
    type = models.CharField(max_length=100, choices=BuildingType)
    area_m2 = models.FloatField(help_text="Floor area in square meters")
    year_built = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_annual_energy_kwh(self, year):
        return sum(m.kwh for m in self.energy_records.filter(date__year=year))

    def get_eui(self, year):
        total_energy = self.get_annual_energy_kwh(year)
        return round(total_energy / self.area_m2, 2) if self.area_m2 else 0

    @property
    def records(self):
        from simplebuildingmanager.records.models import BaseRecord
        return BaseRecord.objects.filter(building=self)
