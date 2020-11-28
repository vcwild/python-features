from sqlite3 import connect
from contextlib import contextmanager


@contextmanager
def temptable(cur):
  cur.execute('CREATE TABLE POINTS(X INT, Y INT)')
  try:
    yield
  finally:
    cur.execute('DROP TABLE POINTS')


with connect('test.db') as conn:
  cur = conn.cursor()
  with temptable(cur):
    cur.execute('INSERT INTO POINTS (X, Y) VALUES(1, 1)')
    cur.execute('INSERT INTO POINTS (X, Y) VALUES(2, 3)')
    cur.execute('INSERT INTO POINTS (X, Y) VALUES(4, 2)')
    for row in cur.execute('SELECT X, Y FROM POINTS'):
      print(row)
    for row in cur.execute('SELECT SUM(X * Y) FROM POINTS'):
      print(row)
