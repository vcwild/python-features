# How to intercept class construction:

# define metaclass feature
class BaseMeta(type):
  def __new__(cls, name, bases, body):
    if not 'bar' in body:
      raise TypeError("Bad user class")
    return super().__new__(cls, name, bases, body)



# try to return .bar() method from Base
class Base(metaclass=BaseMeta):
  def foo(self):
    return self.bar()
