# Model Definition
from django.db import models

class MyModel(models.Model):
    my_tri_state_field1 = models.BooleanField(null=True, blank=True)
    my_tri_state_field2 = models.BooleanField(null=True, blank=True)
    
    class Meta:
        app_label = 'tria'