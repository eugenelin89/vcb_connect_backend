"""
Points ledger models capturing debits/credits per user.
"""

from django.conf import settings
from django.db import models


class PointsTransaction(models.Model):
    """Atomic change to a user's point balance with contextual reason."""

    class Reason(models.TextChoices):
        VOLUNTEER_COMPLETED = "volunteer_completed", "Volunteer completed"
        GAME_WIN_BONUS = "game_win_bonus", "Game win bonus"
        SHOP_REDEEM = "shop_redeem", "Shop redemption"
        MANUAL_ADJUSTMENT = "manual_adjustment", "Manual adjustment"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="points_transactions",
    )
    league = models.ForeignKey(
        "leagues.League",
        on_delete=models.CASCADE,
        related_name="points_transactions",
    )
    delta = models.IntegerField()
    reason = models.CharField(max_length=50, choices=Reason.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user} {self.delta} points ({self.reason})"
