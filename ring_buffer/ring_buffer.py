# Easy way?
# import numpy as np
# from numpy_ringbuffer import RingBuffer



# Define a buffer with a fixed size, so that when it fills up, 
# adding another element must overwrite the first (oldest) one.

# Array that cant grow bigger than starting capacity. Only able to overwrite old vals

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    # add item to storage lists
    self.storage[self.current] = item
    # length of list full/capacity?
    if self.current >= len(self.storage)-1:
          self.current = 0
        else:
          # append an element overwriting oldest one
      self.current += 1

  def get(self):
    # return list of elements we appended to ring buffer
    return [val for val in self.storage if val is not None]



buffer = RingBuffer(5)
buffer.get()


# class RingBuffer:
#   """ class that implements a not-yet-full buffer """
#   def _ _init_ _(self,size_max):
#       self.max = size_max
#       self.data = []

#   class _ _Full:
#       """ class that implements a full buffer """
#       def append(self, x):
#           """ Append an element overwriting the oldest one. """
#           self.data[self.cur] = x
#           self.cur = (self.cur+1) % self.max
#       def get(self):
#           """ return list of elements in correct order """
#           return self.data[self.cur:]+self.data[:self.cur]

#   def append(self,x):
#       """append an element at the end of the buffer"""
#       self.data.append(x)
#       if len(self.data) == self.max:
#           self.cur = 0
#           # Permanently change self's class from non-full to full
#           self._ _class_ _ = self._ _Full

#   def get(self):
#       """ Return a list of elements from the oldest to the newest. """
#       return self.data

