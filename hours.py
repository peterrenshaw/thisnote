#!/usr/bin/env python3
# ~*~ coding: utf-8 ~*~

import time
import datetime


HHMM = "%H%M"

# what is the time LOCALTIME now?
today = datetime.date.today()

hhmm = today.strftime(HHMM)
print("{}".format(hhmm))

# eof
