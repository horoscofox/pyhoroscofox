import base64

CAPRICORN = 'capricorn'
AQUARIUS = 'aquarius'
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
    AQUARIUS,
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
MONTH = 'month'
INFO = 'info'

KINDS = [
    TODAY,
    TOMORROW,
    WEEK,
    MONTH,
    INFO
]

IT_SIGNS = {
    CAPRICORN: 'capricorno',
    AQUARIUS: 'acquario',
    PISCES: 'pesci',
    ARIES: 'ariete',
    TAURUS: 'toro',
    GEMINI: 'gemelli',
    CANCER: 'cancro',
    LEO: 'leone',
    VIRGO: 'vergine',
    LIBRA: 'bilancia',
    SCORPIO: 'scorpione',
    SAGITTARIUS: 'sagittario'
}

PAOLO_URL_ENDPOINT = base64.b64decode(
    '==wL0VmbuAHch1SZ2lGdjFmclRnbp5iMtJnLlJ2LvoDc0RHa'[::-1]
).decode('UTF-8')


BRANKO_URL_ENDPOINT = base64.b64decode(
    '=AHaw5ybw92Yz9mcv9Fdld2L0BXayN2cv82auFmci9GcvN2cvJ3bvIXZ05WZj5ycwBXYkl2byRmbh9yL6MHc0RHa'[::-1]
).decode('UTF-8')


__all__ = [
    'CAPRICORN',
    'AQUARIUS',
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
    'WEEK',
    'MONTH',
    'INFO',

    'IT_SIGNS'
]
