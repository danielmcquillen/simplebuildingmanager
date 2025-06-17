from django.db import models
from django.utils.translation import gettext_lazy as _


class RecordType(models.TextChoices):
    ENERGY = "ENERGY", _("Energy")
    WATER = "WATER", _("Water")
    COST = "COST", _("Cost")
    EMISSIONS = "EMISSIONS", _("Emissions")
