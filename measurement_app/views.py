from utils.base_view import BaseView
import pandas as pd
import json
from measurement_app.db_api import (create_measurementrecord,get_measurementrecord)
from django.core.exceptions import ObjectDoesNotExist
from utils.helpers import (update_db_object,api_success_response,api_error_response)
from accounts.db_api import (get_userprofile,)


class LoadFile(BaseView):

    def post(self,request):
        self.validate_field_in_params(request.FILES,['file'])
        df = pd.read_csv(request.FILES['file'])
        df.fillna(0,inplace=True)
        records_list = json.loads(df.to_json(orient='records'))

        for record in records_list:
            mapped_data = dict()
            for key,value in record.items():
                key = key.strip("(cm)").strip("(kgs)").strip().lower()
                mapped_data.update({key:value})
            try:
                instance = get_measurementrecord(height=mapped_data.get("height",0),
                weight=mapped_data.get("weight",0),age=mapped_data.get("age",0))
                update_db_object(instance,mapped_data)
            except ObjectDoesNotExist:
                create_measurementrecord(**mapped_data)

        return api_success_response(response_data={},message="Measurement Records added successfully")


class WaistMeasurementView(BaseView):

    def get(self,request):
        self.validate_field_in_params(request.GET,["height","weight","age"])

        try:
            user_profile = get_userprofile(user=request.user)
        except ObjectDoesNotExist:
            return api_error_response(error_message="User Profile does not exist for requested use")

        _param_dict = request.GET
        _param_dict = {key: float(value) for key,value in _param_dict.items()}
        try:
            instance = get_measurementrecord(height=_param_dict["height"],weight=_param_dict["weight"],age=_param_dict["age"])
            waist_measurement = instance.waist
            is_waist_measurement_available = True
        except ObjectDoesNotExist:
            is_waist_measurement_available = False
            waist_measurement = 0
        
        if is_waist_measurement_available:
            update_db_object(user_profile,{"waist_measurement":waist_measurement})

        return api_success_response(response_data={
            "is_waist_measurement_available":is_waist_measurement_available,
            "waist_measurement":waist_measurement
        },message="Waist Measurement")

    def patch(self,request):
        self.validate_field_in_params(request.data,["waist_measurement"])
        self.validate_field_in_params(request.GET,["height","weight","age"])
        try:
            user_profile = get_userprofile(user=request.user)
        except ObjectDoesNotExist:
            return api_error_response(error_message="User Profile does not exist for requested use")

        request_data = request.data

        try:
            update_db_object(user_profile,request_data)
            create_measurementrecord(**request.GET)
        except Exception as e:
            return api_error_response(error_message=str(e))

        return api_success_response(response_data={},message="User Profile Updated successfully")
            



        


