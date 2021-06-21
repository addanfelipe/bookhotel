from hotel.types import ClientType
from datetime import datetime
from typing import List, get_args

from wtforms import Form, StringField, ValidationError, validators


class CheapestGetValidator(Form):
    input = StringField('input', [validators.required()])

    def values_input(self, _input: str):
        client_type, dates = _input.split(': ')
        dates = dates.split(', ')
        return client_type, dates

    def check_client_type(self, client_type: str):
        if not client_type in get_args(ClientType):
            raise Exception()

    def str_to_date(self, _date: str):
        _date = _date[:9]  # %d%b%Y(xxx) to %d%b%Y
        return datetime.strptime(_date, '%d%b%Y').date()

    def count_week_weekend(self, dates: List[str]):
        count_week, count_weekend = 0, 0
        for _date in dates:
            _date = self.str_to_date(_date)
            if _date.weekday() < 5:
                count_week += 1
            else:
                count_weekend += 1

        return count_week, count_weekend

    def validate_input(self, field):
        try:
            _input = self.data['input']
            client_type, dates = self.values_input(_input)

            self.check_client_type(client_type)
            count_week, count_weekend = self.count_week_weekend(dates)

            self.client_type: ClientType = client_type
            self.count_week = count_week
            self.count_weekend = count_weekend
        except:
            raise ValidationError('Error Format')
