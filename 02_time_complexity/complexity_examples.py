''' Topic: Time Complexity
    Based off: Time Complexity of While and if #3 by Abdul Bari on Youtube
    What I learnt:
    - In depth understanding of time complexities and how to decipher them from codes
    - Implementation of my concepts into coding examples like counting digits through decimal system and using nested loops
    -Learnt how multiplication and division operations affect time complexity by reducing problem size exponentially  
'''

#Linear Time Complexity O(n)
#returns the sum of all elements in an array
def add_array_elements(L):
    for i in L:
        sum+=i
    return sum

#Quadratic Time Complexity O(n^2)
#prints all the ordered pairs from an array 
def print_op(A):
    for i in range(len(A)):
        for j in range(len(A)):					#using nested loops to index and find all possible pairs from array
            print("(",A[i],",",A[j],")")
            
#Logarithmic Time Complexity O(logn) with base 10
#counts the number of digits in a number
def count(n):
    count=0
    while n>0:
        n=n//10			#Since we are using decimal number system, division is done by 10.If needed to find number of binary digits, division is done by 2 
        count+=1
    print(count)    
