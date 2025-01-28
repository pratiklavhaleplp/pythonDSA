'''
@Goal: write a function to calculate factorial with input value
'''

inputValue = int(input("Enter value: "))

def myFactorial():
  result = 1
  loopPointer = 1
  if inputValue < 0:
    exit()
  while loopPointer <= inputValue:
    result = result * loopPointer
    loopPointer = loopPointer + 1
  return result

print(f'factorial for {inputValue} is: {myFactorial()}')
