import numpy as np
a=np.arange(2,32,2)
print(a)
print("Slicing:",a[2:8])
print("Last 3 Elements:",a[-3:])
a1=a=np.arange(2,32,4)
print("Alternate Numbers:",a1)
print("Last 3 Alternate Numbers:",a1[-3:])
#Create an 1D array with arange containing first 15 even numbers as elements
#a. Elements from index 2 to 8 with step 2(also demonstrate the same
#using slice function)
#b. Last 3 elements of the array using negative index
#c. Alternate elements of the array
#d. Display the last 3 alternate elements
