from measurement_app.models import MeasurementRecord

def create_measurementrecord(*args,**kwargs) -> MeasurementRecord:
    return MeasurementRecord.objects.create(*args,**kwargs)

def get_measurementrecord(*args,**kwargs) -> MeasurementRecord:
    return MeasurementRecord.objects.get(*args,**kwargs)