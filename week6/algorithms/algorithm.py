k = 1
  
pi = 0
  
for i in range(1000000): 

    if i % 2 == 0:
        pi += 4/k

    else: 
  

        pi -= 4/k 

    k += 2
decimalPoint = int(input("Enter the number of decimals to calculate to: "))
newPi = f"{{:.{decimalPoint}f}}".format(pi)
print(newPi) 
