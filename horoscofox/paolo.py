from .constants import SIGNS, KINDS
from .errors import PaoloException
from .sign import Sign


class PaoloClient():

    def __init__(self):
        super().__init__()
        for sign in SIGNS:
            sign_object = Sign(sign)
            setattr(self, sign, sign_object)

    def get(self, sign, kind):
        if sign not in SIGNS:
            raise PaoloException(
                'Sign not allowed, did you mean one of ' + str(SIGNS)
            )
        if kind not in KINDS:
            raise PaoloException(
                'Kind not allowed, did you mean one of ' + str(KINDS)
            )
        sign = getattr(self, sign, None)
        if kind == 'today':
            return sign.today()
        elif kind == 'tomorrow':
            return sign.tomorrow()
        elif kind == 'week':
            return sign.week()
