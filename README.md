<p align="center">
    <h1>PyHoroscofox</h1>
    <br>
    <a href="https://codecov.io/gh/horoscofox/pyhoroscofox">
      <img src="https://codecov.io/gh/horoscofox/pyhoroscofox/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/horoscofox/pyhoroscofox/blob/master/LICENSE">
      <img src="https://img.shields.io/badge/License-MIT-blue.svg" />
    </a>
    <a class="badge-align" href="https://www.codacy.com/app/horoscofox/pyhoroscofox?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=horoscofox/pyhoroscofox&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/54e13d686273408a9e44bb54bb438fdd"/></a>
    <a href="https://travis-ci.org/horoscofox/pyhoroscofox">
      <img src="https://travis-ci.org/horoscofox/pyhoroscofox.svg?branch=master" />
    </a><br>
    <a href="http://forthebadge.com">
      <img src="http://forthebadge.com/images/badges/made-with-python.svg" />
    </a>
</p>

Retrieve your horoscope, written by Paolo Fox and Branko


## How to use 💫

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