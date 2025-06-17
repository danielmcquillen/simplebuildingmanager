# Create your views here.
from typing import Any

from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView

from simplebuildingmanager.core.constants import PublishStatus
from simplebuildingmanager.core.mixins import BreadcrumbMixin
from simplebuildingmanager.courses.models import Course
from simplebuildingmanager.enrollment.forms import SimpleEnrollmentForm


class HomePageView(TemplateView):
    template_name = "marketing/home.html"
    http_method_names = ["get"]

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.filter(publish_status=PublishStatus.PUBLISHED)
        return context


class AboutPageView(BreadcrumbMixin, TemplateView):
    template_name = "marketing/about.html"
    http_method_names = ["get"]
    breadcrumbs = [
        {"name": "About", "url": ""},
    ]
