"""
Volunteer opportunity tracking models.
"""

from django.conf import settings
from django.db import models


class VolunteerSlot(models.Model):
    """Describes a single volunteer opportunity that can be claimed or completed."""

    class Status(models.TextChoices):
        OPEN = "open", "Open"
        CLAIMED = "claimed", "Claimed"
        COMPLETED = "completed", "Completed"

    league = models.ForeignKey(
        "leagues.League",
        on_delete=models.CASCADE,
        related_name="volunteer_slots",
    )
    team = models.ForeignKey(
        "leagues.Team",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="volunteer_slots",
    )
    event_date = models.DateTimeField()
    role_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.OPEN,
    )
    claimed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="claimed_volunteer_slots",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["event_date"]

    def __str__(self) -> str:
        return f"{self.role_name} on {self.event_date:%Y-%m-%d %H:%M} ({self.status})"
