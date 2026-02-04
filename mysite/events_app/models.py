from django.db import models

# Create your models here.
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class EventPage(Page):
    event_date = models.DateField("Event date")
    event_time = models.TimeField("Event time")
    location = models.CharField(max_length=250)
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel("event_date"),
        FieldPanel("event_time"),
        FieldPanel("location"),
        FieldPanel("description"),
    ]