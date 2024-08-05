class Signal:
  """A simple signal class"""
  callbacks = []
  def connect(self, callback):
    def disconnect():
        return self.callbacks.remove(callback)
      
    self.callbacks.append(callback)
    return disconnect
    
  def fire(self, value):
    for callback in self.callbacks:
      callback(value)
    return value

class Storage:
    """A simple storage class"""
    changed = Signal()

    def __init__(self, value):
      self.value = value

    def set(self, value):
      self.value = value
      self.changed.fire(value)

    def update(self, callback):
      value = callback(self.value)
      self.set(value)
      return value

    def increasment(self, value):
      if type(value) != int and float:
        raise Exception(f'{value} must be a number')

      if type(self.value) != int and float:
        raise Exception(f'{self.value} isn`t a number')
        
      def adder(oldValue):
        return oldValue + value
        
      return self.update(adder)

    

currentClass = Storage(1)

def testing(value):
  print(value)

disconnect = currentClass.changed.connect(testing)

print("1st Task")

for x in range(10):
  currentClass.increasment(x)

print("2nd Task")
#disconnect()

for x in range(10):
  currentClass.increasment(-x)

print(f'{100000:.3f}')