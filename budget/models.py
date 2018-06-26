from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    date = models.DateField(default=timezone.now(), blank=False)
    description = models.CharField(default='unknown', blank=False, max_length=50)
    amount = models.FloatField(default=0, blank=False)
    detail = models.CharField(default=None, blank=True, null=True, max_length=100)
    category = models.ForeignKey('Category', default=16, blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            transac = Transaction.objects.filter(
                date = self.date,
                description = self.description,
                amount = self.amount,
                detail = self.detail,
            )
            if not transac:
                super(Transaction, self).save(*args, **kwargs)
        else:
            super(Transaction, self).save(*args, **kwargs)


    def __unicode__(self):
        return u'%s _ [ %s ] _ %s' % (
            self.date.strftime('%y-%m-%d'),
            str(self.amount),
            self.description,
        )


class Category(models.Model):
    name = models.CharField(blank=False, max_length=20)
    description = models.CharField(blank=False, max_length=50)

    def __unicode__(self):
        return u'%s: %s' % (self.name, self.description)
