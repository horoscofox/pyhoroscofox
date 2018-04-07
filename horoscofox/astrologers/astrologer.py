from horoscofox.constants import SIGNS, KINDS
from horoscofox.errors import AstrologerException


class Astrologer():

    def __init__(self):
        for sign in SIGNS:
            sign_object = self.sign_class(sign)
            setattr(self, sign, sign_object)

    def _check_sign(self, sign):
        if sign not in SIGNS:
            raise AstrologerException(
                'Sign not allowed, did you mean one of ' + str(SIGNS)
            )

    def _check_kind(self, kind):
        if kind not in KINDS:
            raise AstrologerException(
                'Kind not allowed, did you mean one of ' + str(KINDS)
            )

    def _get(self, sign, kind):
        raise NotImplementedError()

    def get(self, sign, kind='today'):
        self._check_sign(sign)
        self._check_kind(kind)
        sign_obj = getattr(self, sign, None)
        return self._get(sign_obj, kind)