from .astrologer import Astrologer
from horoscofox.constants import SIGNS
from horoscofox.errors import AstrologerException
from horoscofox.signs.brankosign import BrankoSign


class BrankoClient(Astrologer):

    sign_class = BrankoSign

    def _check_kind(self, kind):
        if kind != "today":
            raise AstrologerException(
                "Sorry, at the moment Branko can see only today's horoscope")

    def _get(self, sign, kind):
        if kind == 'today':
            return sign.today()
