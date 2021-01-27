# PyHoroscofox
![Pyhoroscofox](https://github.com/horoscofox/pyhoroscofox/workflows/Pyhoroscofox/badge.svg)

Retrieve your horoscope, written by Paolo Fox and Branko


## How to use 

```sh
cd pyhoroscofox
pip install -e .
python demo.py
```

#### Get horoscope for Virgo of today and manage response from Paolo
```py
from horoscofox import paolo

virgo_today = paolo.virgo.today()
virgo_today.text
```

Or using the `get` method

```py
import horoscofox
from horoscofox import paolo

virgo_today = paolo.get(sign=horoscofox.VIRGO, kind=horoscofox.TODAY)
virgo_today.text
```

#### If you prefer Branko...

```py
import horoscofox
from horoscofox import branko

virgo_today = branko.virgo.today()
virgo_today.text
```
