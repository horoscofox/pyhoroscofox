from .sign import Sign

import requests
from datetime import datetime,date, timedelta
import calendar 
from horoscofox.constants import PAOLO_URL_ENDPOINT
from horoscofox.errors import AstrologerException
from horoscofox.response import Response
from random import randint


class PaoloSign(Sign):

    def _generic_body(self, kind):
        return {
            "id": str(randint(310000, 9990000)),
            "method": "getContents",
            "params": {
                "config": {
                    "app_uid": "5317e225-47f7-96af8059",
                    "action": kind,
                    "content_provider": "mmdb",
                    "content_type": "text",
                    "service_param": self.sign
                }
            }
        }

    def _generic_request(self, kind):
        try:
            r = requests.post(
                PAOLO_URL_ENDPOINT,
                json=self._generic_body(kind),
            )
            if r.status_code != 200:
                raise AstrologerException('Error using API!')
        except requests.exceptions.ConnectionError:
            raise AstrologerException('Connection error!')
        json_resp = r.json()
        date_start = datetime.strptime(
            json_resp['result']['elem'][0]['content_date'],
            '%Y-%m-%d  %H:%M:%S'
        )
        date_end = None
        if kind == 'daily':
            date_end = date_start + timedelta(days=1)
        elif kind == 'tomorrow':
            date_end = date_start + timedelta(days=1)
        elif kind == 'weekly':
            date_end = date_start + timedelta(days=7)
        elif kind == 'monthly':
            date_end = date_start.replace(day=calendar.monthrange(date_start.year, date_start.month)[1])

        if date_start:
            date_start = date_start.date()

        if date_end:
            date_end = date_end.date()

        return Response(
            json_resp['result']['elem'][0]['text'],
            date_start, date_end
        )


    def _info_request(self):
        try:
            r = requests.post(
                PAOLO_URL_ENDPOINT,
                json=self._generic_body('info'),
            )
            if r.status_code != 200:
                raise AstrologerException('Error using API!')
        except requests.exceptions.ConnectionError:
            raise AstrologerException('Connection error!')
        json_resp = r.json()
        year = date.today().year
        return Response(
            json_resp['result']['elem'][0]['text'],
            datetime(year,1,1).date(),
            datetime(year,12,31).date()
        )
        
    def today(self):
        return self._generic_request('daily')

    def tomorrow(self):
        return self._generic_request('tomorrow')

    def week(self):
        return self._generic_request('weekly')

    def month(self):
        return self._generic_request('monthly')

    def info(self):
        return self._info_request()
