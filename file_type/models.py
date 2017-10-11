from django.db import models
from .base_models import TrackingModel
from django.urls import reverse


class ContentAddressable(TrackingModel):
    file_name = models.CharField(max_length=255, null=False, blank=True)
    file_url = models.URLField(null=False, blank=False)
    file_digest = models.CharField(max_length=64, null=False, blank=False)

    def get_absolute_url(self):
        return reverse('content-addressable-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return "Name: {}, Url: {}, SHA256: {}".format(
            self.file_name, self.file_url, self.file_digest
        )
