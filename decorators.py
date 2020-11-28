from time import time


def timer(func):
  def f(*args, **kwargs):
    before = time() # wrapper function
    rv = func(*args, **kwargs) # wrapped function
    after = time()
    print('elapsed', after - before)
    return rv
  return f


@timer
def add(x, y=10):
  return x + y

@timer
def sub(x, y=10):
  return x - y


print('add(10)', add(10))
print('add(20, 30)', add(20, 30))
print('add(2, 30)', add(2, 30))
print('add(20, 2)', add(20, 2))
print('sub(20, 2)', sub(20, 2))