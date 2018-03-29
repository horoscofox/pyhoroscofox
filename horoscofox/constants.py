import base64


SIGNS = [
    'capricorn',
    'acquarius',
    'pisces',
    'aries',
    'taurus',
    'gemini',
    'cancer',
    'leo',
    'virgo',
    'libra',
    'scorpio',
    'sagittarius'
]
 

URL_ENDPOINT = base64.b64decode(
    '==wL0VmbuAHch1SZ2lGdjFmclRnbp5iMtJnLlJ2LvoDc0RHa'[::-1]
).decode('UTF-8')
