from django.db import models
from django.forms import ModelForm


WEEKDAYS = (('MONDAY','MONDAY'), ('TUESDAY','TUESDAY'), ('WEDNESDAY','WEDNESDAY'), ('THURSDAY','THURSDAY'), ('FRIDAY','FRIDAY'))
NUM_PRAC = tuple((x,x) for x in xrange(0,6))

# Models
class PracticeInfo(models.Model):
    prefOne = models.CharField(max_length=20, choices=WEEKDAYS, blank=False)
    prefTwo = models.CharField(max_length = 20, choices = WEEKDAYS, blank=False)
    prefThree = models.CharField(max_length = 20, choices = WEEKDAYS, blank=False)
    numberOfPracties = models.IntegerField(default=1, choices = NUM_PRAC, 
        blank=False)
    weekendStartTime = models.TimeField(blank=False)

# ModelForms Here

class PracticeInfoForm(ModelForm):
    class Meta:
        model = PracticeInfo
        fields = '__all__'

        
