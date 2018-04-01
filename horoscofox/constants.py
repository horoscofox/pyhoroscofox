import base64

CAPRICORN = 'capricorn'
ACQUARIUS = 'acquarius'
PISCES = 'pisces'
ARIES = 'aries'
TAURUS = 'taurus'
GEMINI = 'gemini'
CANCER = 'cancer'
LEO = 'leo'
VIRGO = 'virgo'
LIBRA = 'libra'
SCORPIO = 'scorpio'
SAGITTARIUS = 'sagittarius'

SIGNS = [
    CAPRICORN,
    ACQUARIUS,
    PISCES,
    ARIES,
    TAURUS,
    GEMINI,
    CANCER,
    LEO,
    VIRGO,
    LIBRA,
    SCORPIO,
    SAGITTARIUS
]

TODAY = 'today'
TOMORROW = 'tomorrow'
WEEK = 'week'

KINDS = [
    TODAY,
    TOMORROW,
    WEEK
]

URL_ENDPOINT = base64.b64decode(
    '==wL0VmbuAHch1SZ2lGdjFmclRnbp5iMtJnLlJ2LvoDc0RHa'[::-1]
).decode('UTF-8')

__all__ = [
    'CAPRICORN',
    'ACQUARIUS',
    'PISCES',
    'ARIES',
    'TAURUS',
    'GEMINI',
    'CANCER',
    'LEO',
    'VIRGO',
    'LIBRA',
    'SCORPIO',
    'SAGITTARIUS',

    'TODAY',
    'TOMORROW',
    'WEEK'
]
