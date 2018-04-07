from .astrologer import Astrologer
from .constants import SIGNS, KINDS
from .errors import AstrologerException
from .signs import PaoloSign


class PaoloClient(Astrologer):

    sign_class = PaoloSign

    def get(self, sign, kind):
        if sign not in SIGNS:
            raise AstrologerException(
                'Sign not allowed, did you mean one of ' + str(SIGNS)
            )
        if kind not in KINDS:
            raise AstrologerException(
                'Kind not allowed, did you mean one of ' + str(KINDS)
            )
        sign = getattr(self, sign, None)
        if kind == 'today':
            return sign.today()
        elif kind == 'tomorrow':
            return sign.tomorrow()
        elif kind == 'week':
            return sign.week()
