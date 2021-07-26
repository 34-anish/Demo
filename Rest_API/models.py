from django.db import models
from django.utils.translation import gettext as _
from datetime import datetime
from django.utils import timezone


# Create your models here.
class DataStock(models.Model):
    # SNo = models.IntegerField(_("SNo"))
    Symbol = models.CharField(_("Symbol"),max_length=50)
    Date = models.DateField(_("Date"), auto_now=True)
    Open = models.FloatField(_("Open"))
    High = models.FloatField(_("High"))
    Low = models.FloatField(_("Low"))
    Close = models.FloatField(_("Close"))
    Vol = models.FloatField(_("Vol"))


class Index(models.Model):
    Index = models.TextField()
    Close = models.FloatField()
    PointChange = models.FloatField()
    PercentageChange = models.FloatField()
    # created_at = models.DateField(default=datetime.now)

class SubIndex(models.Model):
    SubIndex = models.TextField()
    Turnover = models.FloatField()
    Close = models.FloatField()
    PointChange = models.FloatField()
    PercentageChange = models.FloatField()
    # created_at = models.DateField(default=datetime.now)

class TopGainers(models.Model):
    Symbol = models.TextField()
    LTP = models.FloatField()
    PointChange = models.FloatField()
    PercentageChange = models.FloatField()
    # created_at = models.DateField(default=datetime.now)

class TopLoosers(models.Model):
    Symbol = models.TextField()
    LTP = models.FloatField()
    PointChange = models.FloatField()
    PercentageChange = models.FloatField()
    # created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

class TopTurnOvers(models.Model):
    Symbol = models.TextField()
    TurnOvers = models.BigIntegerField()
    LTP = models.FloatField()
    # created_at = models.DateField(default=datetime.now)

class TopTradedShares(models.Model):
    Symbol = models.TextField()
    Volumn = models.BigIntegerField()
    LTP = models.FloatField()
    # created_at = models.DateField(default=datetime.now)

class DatewiseIndex(models.Model):
    Date = models.DateField()
    NepseIndex = models.TextField()
    AbsoluteChange = models.FloatField()
    PercentageChange = models.FloatField()