"""
Suppose you are given two sorted lists of integers. If one array has enough empty entries at its end, it can be used to store the combined entries of the two lists in sorted order. 
For example, consider [5,13,17, None, None, None, None] and [3,7,11,19], where "None" denotes an empty entry. Then the combined sorted entries can be stored in the first list as [3,5,7,11,13,17,19].

Write a method in python as following :

def merge_two_sorted_arrays(nums1:list, m:int, nums2:list, n:int):
to takes as input two sorted lists of int nums1 & nums2, m is number of elements in nums1, n is number of elements in nums2, and updates the first(nums1) to the combined entries of the two arrays in ascending order. Assume the first list has enough empty entries at its end to hold the result.

For example:
Test	Result nums1 = [5,13,17,None,None,None,None,None]
merge_two_sorted_arrays(nums1, 3, [3,7,11,19], 4)
print(nums1[:7])
[3, 5, 7, 11, 13, 17, 19]
nums1 = [-1,None,None,None,None,None,None]
merge_two_sorted_arrays(nums1, 1, [-3,-1,0,3], 4)
print(nums1[:5])
"""

def merge_two_sorted_arrays(nums1:list, m:int, nums2:list, n:int):
    pt1 = m-1
    pt2 = n-1
    pt3 = n+m -1
    
    while pt2 >= 0 and pt1 >= 0:
        if nums1[pt1] >= nums2[pt2]:
            nums1[pt3]  = nums1[pt1]
            pt3 -= 1
            pt1 -= 1
        else:
            nums1[pt3] = nums2[pt2]
            pt3 -= 1
            pt2 -= 1
    if pt2 < 0:
        return 
    else:
        while pt2 >= 0:
            nums1[pt3] = nums2[pt2]
            pt3 -= 1
            pt2 -= 1




"""
Peter received money from his parents this week and wants to spend it all buying books. But he does not read a book so fast, because he likes to enjoy every single word while he is reading. In this way, it
takes him a week to finish a book. As Peter receives money every two weeks, he decided to buy two books, then he can read them until receive more money. As he wishes to spend all the money, he should choose two books whose prices summed up are equal to the money that he has. You can consider that is always possible to find a solution, if there are multiple solutions get the solution that minimizes the difference between the prices of two books. It is a little bit difficult to find these books, so Peter asks your help to find them.

For example, if there were five books with price were $10,$2,$6,$8 and $4, and Peter has money $10, then Peter should buy books whose prices are $4 and $6 in sorted, since 4 + 6 = 10 and 6 - 4 = 2 got the minimum difference in multiple solutions.

Write a method in python as following :

def find_books(prices:list, money:int)->list
to find the books Peter should buy for given prices of books(prices:list) and owned money (money:int), and return the list of two elements of integers in ascending order. If no answer could find, return [-1, -1]

For example:

Test	Result
print(find_books([10,2,6,4,8],10))
[4, 6]
print(find_books([40,40],80))
[40, 40]
"""

def find_books(prices:list, money:int)->list:
    min_diff = float("inf")
    hashtable = {}
    ans = [-1,-1]
    for p in prices:
        if money-p not in hashtable:
            hashtable[p] = 1
        else:
            if abs((money-p)-p) < min_diff:
                min_diff = abs((money-p)-p)
                ans = [money-p,p]
    ans.sort()
    return ans