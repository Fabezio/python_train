# coding:utf-8
"""
  PYTHON

  Synchro
    programmation asynchrone
  """

from datetime import * 
from time import *
from threading import *

myLock = RLock()

class MyProcess(Thread):
  def __init__(self):
    
    Thread.__init__(self)
  
  def run(self):
    i=0
    while i < 5:
      with myLock:
        letters = "ABC" 
        for lt in letters:
          print(i, lt)
          sleep(0.5)
        i += 1
    print("En attente")
    sleep(0.5)


task1 = MyProcess()
task2 = MyProcess()

task1.start()
task2.start()

task1.join()
task2.join()

print("operation.s terminée.s")
