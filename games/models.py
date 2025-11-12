"""
Game scheduling and result models.
"""

from django.db import models


class Game(models.Model):
    """Represents a scheduled game and its outcome for awarding points."""

    class Result(models.TextChoices):
        WIN = "win", "Win"
        LOSS = "loss", "Loss"

    league = models.ForeignKey(
        "leagues.League",
        on_delete=models.CASCADE,
        related_name="games",
    )
    team = models.ForeignKey(
        "leagues.Team",
        on_delete=models.CASCADE,
        related_name="games",
    )
    date = models.DateField()
    opponent = models.CharField(max_length=255)
    result = models.CharField(max_length=10, choices=Result.choices)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date", "team__name"]

    def __str__(self) -> str:
        return f"{self.team.name} vs {self.opponent} on {self.date} ({self.result})"
