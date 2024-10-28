x=int(input("Enter a number : "))
sum_of_odd=0
#if i odd then add it to sum nb 
for i in range (x):
    if i%2!=0:
        #add the odd numbers in sum of odd 
      sum_of_odd += i
print(sum_of_odd)
