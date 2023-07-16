"""
Write a method in python as following :

def two_sum(nums:list, target:int)->list:
Given an list of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

If no answer can be found, return [-1, -1]

For example:

Test	Result
print(two_sum([2,7,11,15],9))
[0, 1]
print(two_sum([3,4,5,2],10))
[-1, -1]
"""

def two_sum(nums:list, target:int)->list:
    hashtable = {}
    n = len(nums)
    for i in range(n):
        if target-nums[i] not in hashtable:
            hashtable[nums[i]] = i 
        else:
            return [hashtable[target-nums[i]],i]
    return [-1,-1]

"""
Write a method in python as following :

def find_nearest_repeated_word(s:list)->int:
Given an list of words, return the distance between a closest pair of equal entries.
If no answer can be found, return -1

For example:

Test	Result
print(find_nearest_repeated_word(["all", "work", "and", "no", "play", "makes", "for", "no", "work", "no", "fun", "and", "no", "results"]))
2
print(find_nearest_repeated_word(["foo", "bar", "widget", "adnan"]))
"""

def find_nearest_repeated_word(s:list)->int:
    near_dis = float("inf")
    hashtable = {}
    n = len(s)

    for i in range(n):
        if s[i] not in hashtable:
            hashtable[s[i]] = i
        else:
            temp_dis = i - hashtable[s[i]]
            hashtable[s[i]] = i
            if temp_dis <= near_dis:
                near_dis = temp_dis
    if type(near_dis) == int:
        return near_dis
    else:
        return -1






