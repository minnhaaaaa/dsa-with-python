'''
Topic: Growth Rate Plots of Time Complexity Functions
Based Off: 1.10.2 Comparison of Functions #2 by Abdul Bari on Youtube
What I learnt:
- The order and growth of classes of functions like O(1),O(n),O(n^2),O(logn),O(nlogn),O(2^n),O(3^n)
- How to use the matplotlibrary to plot a graph of any function in python
- The importance of using a log scale to depict functions of varying growth rates
'''

import matplotlib.pyplot as plt							#imports matplotlib which is commonly used in data science
import numpy as np										

n=np.arange(2,16)										#input values from 2 to 16, essentialy just [2,3,4...,15]
constant=[1 for _ in n]									#cannot be written just as 1, as when plotting it needs to be repeated 14 times
linear=n
quadratic=[i**2 for i in n]
log_n=[np.log2(i) for i in n]							#log base 2 as it is mainly used in computer due to binary system
n_log_n=[i* np.log2(i) for i in n]
exponential=[2**i for i in n]

def plotting():
    plt.plot(n,constant,label="O(1)")					#n is the x value and constant is the y value
    plt.plot(n,linear,label="O(n)")
    plt.plot(n,quadratic,label="O(n^2)")
    plt.plot(n,log_n,label="O(logn)")
    plt.plot(n,n_log_n,label="O(n logn)")
    plt.plot(n,exponential,label="O(2^n)")

def adjust_plot():
    plt.title("Growth Rates of Time Complexity Functions")
    plt.xlabel("Input values (n)")
    plt.ylabel("Operations")
    plt.legend()
    plt.yscale('log')									#log scale is required as slower growing functions will only be seen as straight lines
    plt.show()

plotting()
adjust_plot()
