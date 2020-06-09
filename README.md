<p align="center">
    <h1>PyHoroscofox</h1>
    <br>
    <a href="https://codecov.io/gh/horoscofox/pyhoroscofox">
      <img src="https://codecov.io/gh/horoscofox/pyhoroscofox/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/horoscofox/pyhoroscofox/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
    </a>
    <a href="https://travis-ci.org/horoscofox/pyhoroscofox">
      <img src="https://travis-ci.org/horoscofox/pyhoroscofox.svg?branch=master" />
    </a> 
</p>

Retrieve your horoscope, written by Paolo Fox and Branko


## How to use 

```sh
pip install horoscofox
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
