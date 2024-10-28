x=int(input("Enter a number : "))
sum_of_odd=0
for i in range (x):
    if i%2!=0:
      sum_of_odd += i
print(sum_of_odd)