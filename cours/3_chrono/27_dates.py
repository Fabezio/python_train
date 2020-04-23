# coding:utf-8
"""
  PYTHON

  Synchro
    Gestion des dates
  """

from datetime import * 
from time import *

# chrono defilant
s = 0
while s < 60:
  print (datetime.now())
  sleep(1)
  s += 1

# age
now = date.today()
birth = date(1973, 5, 4)
print((f"Vous avez {now.year - birth.year} ans.")  )