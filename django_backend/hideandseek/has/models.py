from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=32,null=False,unique=True)
    passwd = models.CharField(max_length=128,null=False)
    visible = models.BooleanField(null=False,default=True)
    active = models.BooleanField(null=False,default=True)
    hiddenFrom = models.ManyToManyField('self',related_name="isHiddingFrom")
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)
    z = models.FloatField(null=True)
    acc = models.FloatField(null=True)
    lastSeen = models.DateTimeField(null=True)

    def __unicode__(self):
            return unicode("%s"%self.name)

class PositionLog(models.Model):
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
    z = models.FloatField(null=False)
    acc = models.FloatField(null=False)
    evdate = models.DateTimeField(null=False)
    placedBy = models.ForeignKey(Player,null=False)
    def __unicode__(self):
        args = (self.placedBy.name,self.x,self.y,self.x)
        return unicode("%s:x=%s y=%s z=%s"%args)


class Game(models.Model):
    name = models.CharField(max_length=32,null=False,unique=True)
    ownedBy = models.ForeignKey(Player,related_name='ownsGame')
    passwd = models.CharField(max_length=64,null=True)
    banned = models.ManyToManyField(Player,related_name='bannedFromGame')
    players = models.ManyToManyField(Player,related_name='inGame')
    x = models.FloatField(null=False)
    y = models.FloatField(null=False)
    z = models.FloatField(null=False)
    acc = models.FloatField(null=False)
    radius = models.FloatField(null=True)

    def __unicode__(self):
        return unicode("%s"%self.name)
