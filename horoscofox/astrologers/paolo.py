from .astrologer import Astrologer
from horoscofox.constants import SIGNS, KINDS
from horoscofox.errors import AstrologerException
from horoscofox.signs.paolosign import PaoloSign


class PaoloClient(Astrologer):
    
    sign_class = PaoloSign

    def _get(self, sign, kind):
        if kind == 'today':
            return sign.today()
        elif kind == 'tomorrow':
            return sign.tomorrow()
        elif kind == 'week':
            return sign.week()
