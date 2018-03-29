from .constants import SIGNS
from .errors import PaoloException
from .sign import Sign

KINDS_ALLOWED = ['today', 'tomorrow']


class PaoloClient():

    def __init__(self):
        super().__init__()
        for sign in SIGNS:
            sign_object = Sign(sign)
            setattr(self, sign, sign_object)

    def get(self, sign, kind):
        if sign not in SIGNS:
            raise PaoloException(
                'No sign allowed, did you mean one of '+str(SIGNS))
        if kind not in KINDS_ALLOWED:
            raise PaoloException(
                'No kind allowed, did you mean one of '+str(KINDS_ALLOWED))
        sign = getattr(self, sign, None)
        if kind == 'today':
            return sign.today()
        elif kind == 'tomorrow':
            return sign.tomorrow()
