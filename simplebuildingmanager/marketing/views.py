# Create your views here.
from typing import Any

from django.views.generic import TemplateView

from simplebuildingmanager.core.mixins import BreadcrumbMixin


class HomePageView(TemplateView):
    template_name = "marketing/home.html"
    http_method_names = ["get"]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class AboutPageView(BreadcrumbMixin, TemplateView):
    template_name = "marketing/about.html"
    http_method_names = ["get"]
    breadcrumbs = [
        {"name": "About", "url": ""},
    ]
