from flask import jsonify, Blueprint, request, Flask
from cerberus import Validator
import datetime


class RideMyWay(object):

    def __init__(self):
        '''creating a list containing dictionaries to act as a database'''
        self.rides_list = []


    """
    VALIDATION FOR RIDE DATA
    """

    def add_ride_validation(self, dict_data):
        '''ride data validation function'''
        schema = {
            'starting_point': {
                'type': 'string',
                'required': False,
                'empty': False,
                'maxlength': 25,
                'minlength': 4},
            'destination': {
                'type': 'string',
                'required': False,
                'empty': False,
                'maxlength': 25,
                'minlength': 4}}
        v = Validator(schema)
        v.allow_unknown = True
        return v.validate(dict_data)

    def date_validate(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%d/%m/%Y')
            return True
        except BaseException:
            return False

    def time_validate(self, time_text):
        try:
            datetime.datetime.strptime(time_text, "%H:%M")
            return True
        except BaseException:
            return False

    """
    END OF RIDE CODE
    """
