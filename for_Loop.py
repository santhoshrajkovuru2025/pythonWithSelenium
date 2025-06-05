obj = [2, 1, 3, 4, 5, 7]

for i in obj:
   print(i)
   # print(i*2)
# sum of first 5 natural numbers 1+2+3+4+5 =15
# if range (i,j) => i to j-1

print("******************************************")
summation = 0
for j in range(1, 6):
    summation= summation + j
    print(summation)
print("__________________________________________")

for k in range(1, 10, 15):
    print(k)
    print("skipping the value in K")

for m in range(10):
    print(m)