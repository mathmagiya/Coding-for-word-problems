
"""
A student is paid $32 for the first week if his part-time summer job. For each week after the first, he is paid $80. How many weeks in total does he have to work for his average weekly pay to be $78?

It’s not hard to solve this problem using equation.

Usually I propose additional questions:
x) Write the code to solve this problem (in any language);
xx) Write the code which generates  100 variants of this problem with different set of numbers.

Here is code for xx)
"""
for initial in range (30, 33):
  for current in range (35, 71):
      for final in range (31, 70):
        for n in range (8,100):
          total=(initial+current*(n-1));
          if (total/n==final):
            print("A student is paid $"+str(initial)+" for the first week if his part-time summer job. For each week after the first, he is paid $"+str(current)+". How many weeks in total does he have to work for his average weekly pay to be $"+str(final)+"?\n")
            break;
