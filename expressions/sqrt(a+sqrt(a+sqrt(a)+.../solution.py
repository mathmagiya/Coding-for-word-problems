import math

times = int(input("Enter the number "))
root="math.sqrt(20+"
bracket=")"
expression=""

for i in range(1,times+1):
  expression=expression+root


expression=expression[:-1]+bracket*times

print(eval(expression))
