from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):

    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='given_ratings'
    )

    rated_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_ratings'
    )

    stars = models.IntegerField()

    review = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ['reviewer', 'rated_user']

    def __str__(self):
        return f"{self.reviewer} → {self.rated_user} ({self.stars})"
