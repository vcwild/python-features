# intercept class construction in python 3.6

# define metaclass feature
class BaseMeta(type):
  def __new__(cls, name, bases, body):
    if name != 'Base' and not 'bar' in body:
      raise TypeError("Bad user class")
    return super().__new__(cls, name, bases, body)


# try to return .bar() method from Base
class Base(metaclass=BaseMeta):
  def foo(self):
    return self.bar()

  def __init_subclass__(cls, *args, **kwargs):
    print('init_subclass', args, kwargs)
    return super().__init_subclass__(cls, *args, *kwargs)
