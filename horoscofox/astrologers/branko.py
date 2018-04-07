from .astrologer import Astrologer
from horoscofox.constants import SIGNS
from horoscofox.errors import AstrologerException
from horoscofox.signs.brankosign import BrankoSign


class BrankoClient(Astrologer):

    sign_class = BrankoSign

    def get(self, sign, kind='today'):
        if sign not in SIGNS:
            raise AstrologerException(
                'Sign not allowed, did you mean one of ' + str(SIGNS)
            )
        if kind != "today":
            raise AstrologerException(
                "Sorry, at the moment Branko can see only today's horoscope")
        sign = getattr(self, sign, None)
        if kind == 'today':
            return sign.today()
