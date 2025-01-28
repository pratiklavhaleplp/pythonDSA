'''
@author: Pratik Lavhale
@Goal: 
  a) Accept masses of two objects in kgs, distance between them in meters
  b) Do a validation check
  c) Compute gravitation force between two objects
  d) Print the result
'''


def main() -> None: 
  '''
    @input: None
    @output: None
    @goal: A driver function of application
  '''
  m1 = float(input("Enter mass of first object in kgs"))
  m2 = float(input("Enter mass of second object in kgs"))
  r = float(input("Enter the distance between two objects in meters"))

  try: 
    F = computeGravitationalForce(m1, m2, r)
  except:
    print(exc_name.__name__, exc_data, sep = ':')
    sys.exit(-1)
  print(f"Force between two objects is: {F}")


main()