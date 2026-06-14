from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    TYPE=[
        ('Lost','Lost'),
        ('Found','Found')
    ]

    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posted_items'
    )

    claimed_by=models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='claimed_items'
    )

    title=models.CharField(max_length=100)

    item_type=models.CharField(
        max_length=20,
        choices=TYPE
    )

    description=models.TextField()

    location=models.CharField(
        max_length=100
    )

    image=models.ImageField(
        upload_to='items/'
    )

    contact=models.CharField(
        max_length=30
    )

    claimed=models.BooleanField(
        default=False
    )

    def __str__(self):
        return self.title