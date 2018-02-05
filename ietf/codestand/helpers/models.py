from django.db import models

#class created to get data from dynamic sql query
class Number(models.Model):

    number = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.additional_information
