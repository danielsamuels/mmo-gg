from django.contrib.auth.models import User
from django.db import models


class Type(models.Model):

    name = models.CharField(
        max_length=16,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ("name",)


class Level(models.Model):

    level = models.PositiveIntegerField(
        max_length=16,
        unique=True
    )

    xp = models.PositiveIntegerField(
        "XP Required",
        max_length=16,
        default=0,
    )

    def __unicode__(self):
        return 'Level {}'.format(self.level)

    class Meta:
        ordering = ("level",)


class Character(models.Model):

    user = models.ForeignKey(User)

    name = models.CharField(
        max_length=16,
        db_index=True,
    )

    type = models.ForeignKey(
        Type,
    )

    level = models.PositiveIntegerField(
        max_length=10,
        default=1,
        blank=True
    )

    xp = models.PositiveIntegerField(
        "Current XP",
        max_length=16,
        default=0,
        blank=True
    )

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = (("user", "name"),)
        ordering = ("-level", "name", "pk")
