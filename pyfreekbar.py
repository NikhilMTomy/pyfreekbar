#!/usr/bin/env python

import time
import sys
from modules import freektime
from modules import freekcolors
from modules import freekbat

while True:
  left='%{l} '
  center='%{c}'
  right = (
      '%{r}' 
      ' '
      '' + freekbat.getbat() + ''
      ' '
      '' + freektime.gettime() + ''
      ' '
      )

  left = ' ' + left

  sys.stdout.write("{0}{1}{2}\n".format(left, center, right))
  sys.stdout.flush()

  time.sleep(1)
