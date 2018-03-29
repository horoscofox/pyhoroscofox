import requests
from datetime import datetime, timedelta

from .constants import URL_ENDPOINT
from .response import Response

class Sign():

    def __init__(self, sign):
        self.sign = sign

    def _generic_body(self, kind):
        return {
            "id": "5713030",
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
        r = requests.post(
            URL_ENDPOINT, 
            json=self._generic_body(kind),
        )
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
        # elif kind == 'monthly':
        #     date_end = date_start + timedelta(days=28)
            
        return Response(
            json_resp['result']['elem'][0]['text'], 
            date_start, date_end
        )

    def today(self):
        return self._generic_request('daily')

    def tomorrow(self):
        return self._generic_request('tomorrow')

    # def week(self):
    #     return self._generic_request('weekly')
    
    # def month(self):
    #     return self._generic_request('monthly')