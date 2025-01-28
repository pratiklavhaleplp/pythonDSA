'''
@Goal: write a function to calculate n choose r 
'''

totalNumberOfItems = int(input("Enter total number of items: "))
numberOfItemsToChoose = int(input("Enter items you want to choose: "))

def myFactorial():
  result = 1
  loopPointer = 1
  if numberOfItemsToChoose < 0:
    exit()
  while loopPointer <= numberOfItemsToChoose:
    result = result * loopPointer
    loopPointer = loopPointer + 1
  return result

def nChooseR():
  numberOFCombinations = myFactorial()