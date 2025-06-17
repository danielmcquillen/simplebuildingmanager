import datetime

import pytest

from simplebuildingmanager.buildings.models import Building
from simplebuildingmanager.records.models import CostRecord, EmissionRecord, EnergyRecord, WaterRecord


@pytest.mark.django_db
class TestRecordModels:
    def setup_method(self):
        self.building = Building.objects.create(
            name="Test Library", type="Library", area_m2=2000, year_built=1995, location="Melbourne"
        )
        self.test_date = datetime.date(2024, 1, 1)

    def test_create_energy_record(self):
        record = EnergyRecord.objects.create(
            building=self.building,
            date=self.test_date,
            kwh=12000.0,
            source="electricity",
        )
        assert record.kwh == 12000.0
        assert self.building.energy_records.count() == 1

    def test_create_water_record(self):
        record = WaterRecord.objects.create(
            building=self.building, date=self.test_date, cubic_meters=30.0, source="municipal"
        )
        assert record.cubic_meters == 30.0
        assert self.building.water_records.count() == 1

    def test_create_cost_record(self):
        record = CostRecord.objects.create(
            building=self.building, date=self.test_date, amount=1234.56, category="electricity"
        )
        assert float(record.amount) == 1234.56
        assert self.building.cost_records.count() == 1

    def test_create_emission_record(self):
        record = EmissionRecord.objects.create(
            building=self.building, date=self.test_date, kg_co2e=800.0, method="calculated"
        )
        assert record.kg_co2e == 800.0
        assert self.building.emission_records.count() == 1
