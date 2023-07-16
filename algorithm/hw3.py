"""
To protect ourselves against the COVID-19 virus, we need to keep a social distance from others. Due to the safe social distance required, seats must be rearranged by one seat apart, including the pre-arranged seats.

Write a method in python as following :

def available_seats(seats:list)->int:
Given an integer list of seats containing 0's and 1's, where 0 means empty and 1 means pre-arranged seat. Please return the maximum number of seats without violating the no-adjacent-seats rule, not including pre-arranged.
For example,
[1,0,0,0,1] are three unassigned seats, but in order to maintain social distance, only the middle one can be arranged as a seat, so return 1;
Given [0,0,1,0,0],  the middle is pre-arranged, the leftmost and rightmost seats can meet the epidemic prevention regulations, so return 2.
Hint: Greedy
For example:

Test	Result
print(available_seats([1,0,0,0,1]))
1
print(available_seats([0,0,1,0,0]))
2
"""
def available_seats(seats:list)->int:
    count = 0
    seats2 = seats[:]
    length = len(seats2)
    if length == 1:
        if seats[0] == 0:
            return 1
    elif length == 2:
        if seats[0] == 0 and seats[1] == 0:
            return 1
    else:
        for i in range(length):
            if i == 0:
                if seats2[i] == 0 and seats2[i+1]==0:
                    seats2[i] = 1
                    count += 1
            elif i == length-1:
                if seats2[i] == 0 and seats2[i-1] ==0:
                    seats2[i] = 1
                    count += 1
            else:# i >= 1 and i <=length -2
                if seats2[i-1]== 0  and seats2[i] == 0 and seats2[i+1]==0:
                    seats2[i] = 1
                    count += 1
    return count


"""A sequence of n > 0 integers is called a jolly jumper if the absolute values of the difference between successive elements take on all the values 1 through n-1. For instance,
1 4 2 3
is a jolly jumper, because the absolutes differences are 3, 2, and 1 respectively. The definition implies that any sequence of a single integer is a jolly jumper. You are to write a program to determine whether or not each of a number of sequences is a jolly jumper.

Write a method in python as following :

def is_jolly_jump(nums:list)->bool:
to determine the input list of integers nums is jolly jumper(True) or not(False).

For example:

Test	Result
print(is_jolly_jump([1,4,2,3]))
True
print(is_jolly_jump([4,1,4,2,3]))
False

"""
def is_jolly_jump(nums:list)->bool:
    length = len(nums)
    result = [0]*(length-1)
    for i in range(1,length):
        diff = abs(nums[i] - nums[i-1])
        if diff-1 < 0 or diff-1 >length-2:
            return False
        result[diff-1] = 1
    if result.count(1) == length-1:
        return True
    else:
        return False

