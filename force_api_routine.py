from api_mock import first, second, last


# define api context
class Api:
  def run_this_first(self):
    first()


  def run_thissecond(self):
    second()


  def run_this_last(self):
    last()

# force api to yield each iterator, one by one
def run_api():
  first()
  yield
  second()
  yield
  last()