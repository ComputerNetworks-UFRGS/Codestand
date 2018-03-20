from django.db import models

#class created to get data from dynamic sql query
class Number(models.Model):

    number = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.additional_information

class StringValue(models.Model):

    stringValue = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.additional_information
