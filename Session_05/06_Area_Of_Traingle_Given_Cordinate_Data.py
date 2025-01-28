import sys

x1 = float(input('Enter x1 coordinate of point A: '))
y1 = float(input('Enter y1 coordinate of point A: '))
x2 = float(input('Enter x2 coordinate of point B: '))
y2 = float(input('Enter y2 coordinate of point B: '))
x3 = float(input('Enter x3 coordinate of point C: '))
y3 = float(input('Enter y3 coordinate of point C: '))


# Two point formula for finding slopw
slope_AB = abs((y2-y1)/(x2-x1))
slope_AC = abs((y3-y1)/(x3-x1))

if slope_AB == slope_AC:
  print("A, B, C are in one line")
  sys.exit()

# side a: distance(B, C), side b: distance(C, A), side c: distance(A, B)
a = ((x3-x2)**2 + (y3-y2)**2) ** 0.5
b = ((x3-x1)**2 + (y3-y1)**2) ** 0.5
c = ((x2-x1)**2 + (y2-y1)**2) ** 0.5
s = (a+b+c)/2

area = (s *(s-a) * (s-b)*(s-c))**0.5

print(f'Area of traingle is {area}')