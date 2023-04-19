from django.db import models
from utils.base_model import BaseModel

class MeasurementRecord(BaseModel):

    height = models.DecimalField(decimal_places=3,max_digits=20,default=0)
    weight = models.DecimalField(decimal_places=3,max_digits=20,default=0)
    age = models.DecimalField(decimal_places=3,max_digits=20,default=0)
    waist = models.DecimalField(decimal_places=3,max_digits=20,default=0)