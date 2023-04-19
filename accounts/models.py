from utils.base_model import BaseModel
from django.contrib.auth.models import User
from django.db import models

class UserProfile(BaseModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    waist_measurement = models.DecimalField(decimal_places=3,max_digits=20,default=0)
