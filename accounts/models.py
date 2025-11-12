"""
Account-related data models.
"""

from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    """Extension model that stores league context and gamification stats per user."""

    class Role(models.TextChoices):
        PLAYER = "player", "Player"
        COACH = "coach", "Coach"
        ADMIN = "admin", "Admin"

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PLAYER,
    )
    league = models.ForeignKey(
        "leagues.League",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_profiles",
    )
    team = models.ForeignKey(
        "leagues.Team",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_profiles",
    )
    points = models.IntegerField(default=0)
    current_streak = models.IntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"UserProfile({self.user}, role={self.role})"
