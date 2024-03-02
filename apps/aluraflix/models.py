from django.db import models


class Program(models.Model):
    TYPE = (
        ('F', 'Film'),
        ('S', 'Series'),
    )

    title = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=1, choices=TYPE, null=False, blank=False, default='F')  # noqa: E501
    release_date = models.DateField()
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.title}'
