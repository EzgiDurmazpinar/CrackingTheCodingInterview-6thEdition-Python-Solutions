#16.7
#Number Max: Write a method that finds the maximum of two numbers. You should not use if-else or any other comparison operator.

def number_max(a, b):
  diff = b - a
  sign = (diff & (1 << 63)) >> 63
  return a * sign + b * (sign ^ 1)
