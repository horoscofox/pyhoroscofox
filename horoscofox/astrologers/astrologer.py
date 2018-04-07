from horoscofox.constants import SIGNS
from horoscofox.errors import AstrologerException


class Astrologer():

    def __init__(self):
        for sign in SIGNS:
            sign_object = self.sign_class(sign)
            setattr(self, sign, sign_object)
