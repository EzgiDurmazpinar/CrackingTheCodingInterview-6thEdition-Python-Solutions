# Implement operations with only addition (and negation).

def multiply(a, b):
  if abs(a) < abs(b):
    s, l = a, b
  else:
    s, l = b, a
  product = 0
  for _ in xrange(abs(s)):
    product += l
  if s < 0:
    return -product
  return product

def divide(a, b):
  if b == 0:
    return None
  product = 0
  quotient = 0
  while product + abs(b) < abs(a) + 1:
    product += abs(b)
    quotient += 1
  if int(a < 0) + int(b < 0) == 1:
    return -quotient
  return quotient

def subtract(a, b):
  return a + (-b)
