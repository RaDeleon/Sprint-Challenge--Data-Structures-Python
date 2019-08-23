# Easy way?
# import numpy as np
# from numpy_ringbuffer import RingBuffer



class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # add item to storage lists
    self.storage[self.current] = item
    if self.current >= len(self.storage)-1:
          self.current = 0
    else:
      self.current += 1

  def get(self):
    return [val for val in self.storage if val is not None]



buffer = RingBuffer(5)
buffer.get()
