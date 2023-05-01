import math #imporing this library to use the ceiling function
import big_o # to find the time complexity of the program
def kthSmallest(array, l, r, k):  #creating a function kthsmallest to calculate
      
    if (k > 0 and k <= r - l + 1):  
        n = r - l + 1
        median = [] 
        i = 0
        while (i < math.ceil(n // 5)): # change 3 to the required number of dividings.
            median.append(Median(array, l + i * 5, 5)) 
            i += 1
        if (i * 5 < n): 
            median.append(Median(array, l + i * 5, n % 5)) 
            i += 1
        if i == 1: 
            medOfMed = median[i - 1] 
        else: 
            medOfMed = kthSmallest(median, 0, i - 1, i // 2)    
        pos = dividing(array, l, r, medOfMed) 
        if (pos - l == k - 1):  
            return array[pos]  
        if (pos - l > k - 1): 
            return kthSmallest(array, l, pos - 1, k)  
        return kthSmallest(array, pos + 1, r, k - pos + l - 1)  
    return 9999         #returning if the value is more that the number given
  
def Median(array, l, n): # finding the median using using the function in the array
    lis = [] 
    for i in range(l, l + n): 
        lis.append(array[i]) 
    lis.sort() 
    return lis[n // 2] # ceiling the value to find the median

def dividing(array, l, r, x):   # dividing the array further in baby medians
    for i in range(l, r): 
        if array[i] == x: 
            swapping(array, r, i) 
            break
    x = array[r]  
    i = l  
    for j in range(l, r):  
        if (array[j] <= x):  
            swapping(array, i, j)  
            i += 1
    swapping(array, i, r)  
    return i  

def swapping(array, a, b):  # swapping the array by using the function
    temp = array[a]  
    array[a] = array[b]  
    array[b] = temp    


   
lines = []
numbers =[]
with open('/Users/affanmoyeed/Desktop/hw#cs5310Moyeed030822/test_hw3.txt') as f:
    lines = f.readlines()

for line in lines:
    numbers.append(int(line))
nums_copy=numbers
k = input("Enter k value to find:")
k = int(k)
length=len(numbers)

if(k>length):
    print("Index not found")
else:
    print("kth smallest element is ",kthSmallest(nums_copy,0,length-1,k)) 

#Generating random test strings of length 100
sample_strings = lambda n: big_o.datagen.strings(100)
#my logic to find the first non-repetitive character in the string
def non_repetitive(sample_string):
    string_list = list(sample_string)
    non_repetitive_char = next((ele for ele in string_list if string_list.count(ele)==1),None)
    return non_repetitive_char
#Calculating the Time complexity
best, others = big_o.big_o(non_repetitive, sample_strings,n_measures=20)
print(best)



#output
#Constant: time = 2.2E-05 (sec)
#Linear: time = 2.9E-05 + -1.3E-10*n (sec)
#Quadratic: time = 2.4E-05 + -6.2E-16*n^2 (sec)
#Cubic: time = 2.3E-05 + -3.6E-21*n^3 (sec)
#Polynomial: time = -8.9 * x^-0.19 (sec)
#Logarithmic: time = 9.1E-05 + -6.7E-06*log(n) (sec)
#Linearithmic: time = 2.8E-05 + -1E-11*n*log(n) (sec)
#Exponential: time = -11 * -3.7E-06^n (sec)