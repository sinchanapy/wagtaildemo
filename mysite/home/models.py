from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    subpage_types = ['events_app.EventPage']
    body = RichTextField(blank=True)
    livingroom = RichTextField(blank=True)

    content_panels = Page.content_panels + ["body","livingroom"]