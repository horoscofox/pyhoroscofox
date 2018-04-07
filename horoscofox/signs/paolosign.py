from .sign import Sign

import requests
from datetime import datetime, timedelta

from horoscofox.constants import PAOLO_URL_ENDPOINT
from horoscofox.errors import AstrologerException
from horoscofox.response import Response
from random import randint


class PaoloSign(Sign):

    def _generic_body(self, kind):
        return {
            "id": str(randint(330000, 9900000)),
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

        if date_start:
            date_start = date_start.date()

        if date_end:
            date_end = date_end.date()

        return Response(
            json_resp['result']['elem'][0]['text'],
            date_start, date_end
        )

    def today(self):
        return self._generic_request('daily')

    def tomorrow(self):
        return self._generic_request('tomorrow')

    def week(self):
        return self._generic_request('weekly')