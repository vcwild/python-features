from time import sleep


def calculate():
  for i in range(10):
    sleep(.5)
    yield i


for val in calculate():
  print(val)
