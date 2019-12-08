
"""
A student is paid $32 for the first week if his part-time summer job. For each week after the first, he is paid $80. How many weeks in total does he have to work for his average weekly pay to be $78?

It’s not hard to solve this problem using equation.

Usually I propose additional questions:
x) Write the code to solve this problem (in any language);
xx) Write the code which generates  100 variants of this problem with different set of numbers.

Here is code for x)
"""

for n in range (2,2000):
  a=(32+80*(n-1));
  print("day: "+str(n)+"; total money: "+str(a)+"\nmean:"+str(a/n)+"\n") #current day
  if (a/n==78):
    break;
print("Answer:"+str(n))
