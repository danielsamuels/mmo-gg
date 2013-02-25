from django.db import models

class Spells(models.Model):

    name = models.CharField(
        max_length=16,
    )

    mana_cost = models.IntegerField(
        max_length=16,
    )


class Family(models.Model):

    name = models.CharField(
        max_length=16,
    )

    def __unicode__(self):
        return self.name


class Type(models.Model):

    name = models.CharField(
        max_length=16,
    )

    family = models.ForeignKey(Family)

    def __unicode__(self):
        return self.name


class Enemy(models.Model):

    user = models.ForeignKey(User)

    name = models.CharField(
        max_length=16,
    )

    type = models.ForeignKey(Type)

    level = models.IntegerField(
        max_length=16,
        default='1'
    )

    current_hp = models.IntegerField(
        max_length=16,
    )

    max_hp = models.IntegerField(
        max_length=16,
    )

    def __unicode__(self):
        return self.name
