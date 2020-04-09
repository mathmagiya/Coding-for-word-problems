def sumOfSeries(start, end, gap):
  sumOf=0
  for i in range(start, end+1, gap):
    sumOf=sumOf+i
  return sumOf

sumOfSeries(2, 4, 1)
gap=1
start=1
end=120
arr1=[]
#sum1=0
print("=====================")
for i in range(start, end, gap):
  arr1.append(i)
  sum1=sumOfSeries(start, i, gap)
  sum2=0
  arr2=[]
  for k in range(i+2*gap, end+1, gap):
    arr2.append(k)
    sum2=sumOfSeries(i+2*gap, k, gap)
    if(sum2==sum1):
      print("FOUND! ",arr1, i+gap, arr2, sum1)
      sum1=0
      break
    if(sum2>sum1):
      sum1=0
      break

