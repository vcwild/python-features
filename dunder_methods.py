class Polynomial:
  def __init__(self, *coeffs):
    self.coeffs = coeffs

  def __str__(self):
    return f'{self.__class__.__name__}(*{str(self.__dict__)})'

  def __repr__(self):
    return f'{self.__class__!r}(*{str(self.__dict__)!r})' #!r evokes repr() method

  def __add__(self, other):
    return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

  def __len__(self):
    return len(self.coeffs)

  def __call__(self):
    pass



p1 = Polynomial(1, 2, 3)
p2 = Polynomial(3, 4, 3)