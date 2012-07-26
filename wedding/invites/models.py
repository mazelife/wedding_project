from django.db import models


class RSVP(models.Model):
    """
    A model of an RSVP.
    """
    name = models.CharField(max_length=300, unique="True")
    attending = models.BooleanField()
    guests = models.SmallIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "RSVP"

    def __unicode__(self):
        return self.name
