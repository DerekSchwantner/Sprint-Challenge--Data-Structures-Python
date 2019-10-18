class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      # sets the item at the current index to item parameter
      self.storage[self.current] = item
      # if below capacity, current index will increment
      if self.current < self.capacity - 1:
        self.current += 1
      else:
        self.current = 0

      return self.storage

  def get(self):
      return [i for i in self.storage if i]


buffer = RingBuffer(5)

print(buffer.get())   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')
print(buffer.get())   # should return ['a', 'b', 'c', 'd']

# 'e' brings buffer to the limit
buffer.append('e')
print(buffer.get())  # should return ['a', 'b', 'c', 'd', 'e']

# 'e' overwrites the oldest value in the ring buffer and returns ['a', 'b', 'c', 'd', 'e']

buffer.append('f')
buffer.append('g')
buffer.append('h')
buffer.append('i')

print(buffer.get())   # should return ['d', 'e', 'f']

# need to add incrementing when at capacity
# def append(self, item):
#   if self.current == self.capacity:
#     del self.storage[0]
#     self.current -= 1
#     self.storage.append(item)
#     self.current += 1
#   else:
#     self.current += 1
#     del self.storage[0]
#     self.storage.append(item)
#
#   return self.storage