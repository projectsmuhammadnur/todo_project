from django.db import models


class Todos(models.Model):
    user_id = models.ForeignKey("users.User", on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    memo = models.TextField(null=True)
    important = models.BooleanField(default=False, null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return f"{self.title}"
