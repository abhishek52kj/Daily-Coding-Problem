def cons(a, b):

  def pair(f):
    return f(a, b)

  return pair


def car(pair):

  def get_first(a, b):
    return a

  return pair(get_first)


def cdr(pair):

  def get_last(a, b):
    return b

  return pair(get_last)


pair = cons(3, 4)
print("car:", car(pair))  # Output: 3
print("cdr:", cdr(pair))  # Output: 4
