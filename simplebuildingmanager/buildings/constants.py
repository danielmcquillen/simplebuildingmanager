from django.db import models
from django.utils.translation import gettext_lazy as _


class BuildingType(models.TextChoices):
    OFFICE = "OFFICE", _("Office")
    RETAIL = "RETAIL", _("Retail")
    INDUSTRIAL = "INDUSTRIAL", _("Industrial")
    RESIDENTIAL = "RESIDENTIAL", _("Residential")
    OTHER = "OTHER", _("Other")
