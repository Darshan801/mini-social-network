from django.conf import settings
from django.db import models

class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='sent_requests',
        on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='received_requests',
        on_delete=models.CASCADE
    )
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.from_user} → {self.to_user}"

User = settings.AUTH_USER_MODEL

class FriendRequest(models.Model):
    from_user = models.ForeignKey(
        User, related_name='sent_requests', on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name='received_requests', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.from_user} → {self.to_user}"
