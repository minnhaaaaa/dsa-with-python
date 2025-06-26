'''Topic: Linear and Binary Search
   Based Off: 1.11 Best Worst and Average Case Analysis by Abdul Bari on Youtube
   Time Complexity: O(logn)
   What I learnt:
   -How to analyse best and worst case time complexities
   -How to implement binary search to find an element easily
'''

def linear_search(n,L):
    for i in range (len(L)):
        if L[i]==n:
            return f"Element found at index {i}"
    return("Not Found")
#The best case in this function would be if the required element is at the 0th index which is O(1)
#The worst case is if the required element is at the last index which is O(n)

def binary_search(n,L):       #Binary search only works if list L is sorted
    print(L)
    b=0
    e=len(L)-1
    while b<=e:
        mid=(b+e)//2
        if L[mid]==n:
            return f"Element found at index {mid}"
        elif L[mid]<n:
            b=mid+1
        else:
            e=mid-1
    return ("Not Found")
#The best case would be if n was the middle element of the list which is O(1)
#The worst case would be if n was not present in the list which is O(logn)

