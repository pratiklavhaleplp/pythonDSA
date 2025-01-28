from math import factorial as fact
from sys import exit


def nChooseR(n: int, r: int):
  if n < 0 or r < 0:
    exit()
  if n < 0:
    return 0
  numberOfCombinations = fact(n)//(fact(r) * fact(n-r))
  return numberOfCombinations

print(nChooseR(10, 3))
print(nChooseR(25, 4))
