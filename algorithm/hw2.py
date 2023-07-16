"""
Write a method in python as following :

def reverse_digits(x:int)->int:
to return the integer corresponding to the digits of the input x written in reverse order.

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

For example:

Test	Result
print(reverse_digits(42))
24
print(reverse_digits(-314))
-413
"""
def reverse_digits(x:int)->int:
    ans = 0
    x2 = x if x>0 else x*-1
    while( x2 != 0):
        r = x2 % 10
        #print(r)
        ans = ans * 10 + r
        
        x2 = int(x2/10)
    if ans < (-2)**31 or ans > ((2)**31)-1 :
        return 0
    elif x >= 0:
        return ans 
    else:
        return -1*ans


"""Consider the following algorithm:
1. input n
2. print n
3. if n = 1 then STOP
4.     if n is odd then n = 3n + 1
5.     else n = n/2
6. GOTO 2

Given the input 22, the following sequence of numbers will be printed
22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
It is conjectured that the algorithm above will terminate (when a 1 is printed) for any integral input value. Despite the simplicity of the algorithm, it is unknown whether this conjecture is true. It has been verified, however, for all integers n such that 0 < n < 1,000,000 (and, in fact, for many more numbers than this.)

Given an input n, it is possible to determine the number of numbers printed before and including the 1 is printed. For a given n this is called the cycle-length of n. In the example above, the cycle length of 22 is 16.

For any two numbers i and j you are to determine the maximum cycle length over all numbers between and including both i and j.

Write at least one method in python as following :

def get_largest_cycle(i:int, j:int)->int:
to return the maximum cycle length for integers between and including input integers i and j. (i, j are less than 1,000,000 and greater than 0)

For example:

Test	Result
print(get_largest_cycle(1,10))
20
print(get_largest_cycle(100,200))
125"""
def get_largest_cycle(i:int, j:int)->int:
    def length(n:int):
        count = 0
        while(n!=1):
            if n % 2  == 1:
                n = 3*n + 1
            else:
                n = n/2
            count += 1
        return count
    maximum = 0
    l = min(i,j)
    r = max(i,j)
    for index in range(l,r+1):
        temp = length(index)
        if temp >= maximum:
            maximum = temp
        
    return maximum+1