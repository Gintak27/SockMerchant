import sys
import array 


print("Hello, Visual Studio")
#pop from list check if popped value is in list 
#if its in the list remove it amd add to count 

def sockMerchant(n, ar):
    count = 0
    while (len(ar)>1):
        a = ar.pop()
        if (a in ar):
            count+= 1
            ar.remove(a)

    print(count)

arr = array.array('i',  [10, 20, 20, 10, 10, 30, 50, 10, 20])

sockMerchant(7,arr)



