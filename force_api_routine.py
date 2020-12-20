from api_mock import first, second, last


# define api context
class Api:
  def run_this_first(self):
    first()


  def run_this_second(self):
    second()


  def run_this_last(self):
    last()

# force api to yield for every step in between routines
def run_api():
  first()
  yield
  second()
  yield
  last()
