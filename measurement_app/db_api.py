from measurement_app.models import MeasurementRecord
from django.db.models.query import QuerySet

def create_measurementrecord(*args,**kwargs) -> MeasurementRecord:
    return MeasurementRecord.objects.create(*args,**kwargs)

def get_measurementrecord(*args,**kwargs) -> MeasurementRecord:
    return MeasurementRecord.objects.get(*args,**kwargs)

def filter_measurementrecord(*args,**kwargs) -> QuerySet:
    return MeasurementRecord.objects.filter(*args,**kwargs)