"""
Shop catalog models for point redemptions.
"""

from django.db import models


class StoreItem(models.Model):
    """Merch or reward items available for point redemption."""

    league = models.ForeignKey(
        "leagues.League",
        on_delete=models.CASCADE,
        related_name="store_items",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price_cents = models.IntegerField()
    points_discount_allowed = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name
