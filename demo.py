import horoscofox
from horoscofox import paolo


print ('♏️  Scorpio Today')
scorpio_today = paolo.scorpio.today()
print (scorpio_today.date_start)
print (scorpio_today.date_end)
print (scorpio_today.text)

print ('♏️  Scorpio Tomorrow')
scorpio_tomorrow = paolo.scorpio.tomorrow()
print (scorpio_tomorrow.date_start)
print (scorpio_tomorrow.date_end)
print (scorpio_tomorrow.text)

print ('♍️  Virgo Today')
virgo_today = paolo.get(sign=horoscofox.VIRGO, kind=horoscofox.TODAY)
print (virgo_today.text)
