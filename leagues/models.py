"""
League and team domain models.
"""

from django.conf import settings
from django.db import models


class League(models.Model):
    """Top-level organization managing teams and volunteer activity."""

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Team(models.Model):
    """Represents a team within a league, optionally scoped to a division."""

    league = models.ForeignKey(
        League,
        on_delete=models.CASCADE,
        related_name="teams",
    )
    name = models.CharField(max_length=255)
    division = models.CharField(max_length=50, blank=True)
    coach = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="coached_teams",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["league__name", "name"]
        unique_together = ("league", "name")

    def __str__(self) -> str:
        return f"{self.league.slug} - {self.name}"
