from django.urls import path
from measurement_app.views import LoadFile,WaistMeasurementView
app_name="measurement_app"

urlpatterns = [
    path('load-file/',LoadFile.as_view(),name="load-file"),
    path('waist-measurement/',WaistMeasurementView.as_view(),name="waist-measurement"),
]