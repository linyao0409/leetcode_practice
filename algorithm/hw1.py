"""
Write a method in python as following :

def count_bits(n:int)->int:
Given a positive integer n, please count the number of bits that are set to 1 in n, and then return the result.

For example:

Test	Result
print(count_bits(5))
2
print(count_bits(15))
4
"""
def count_bits(n:int)->int:
    temp = n
    ans = 0
    while(temp != 0):
        
        if temp & 1 == 1:
            ans += 1
        
        temp = temp>>1

    return ans

"""Write a method in python as following :

def is_valid_word(word:str, tiles:str)->bool:
Given two strings word and tiles, return True if the word can be made with the characters in tiles you’re given, otherwise return False.

Every characters in tiles can use only once to form the word.

For example:

Test	Result
print(is_valid_word('ART','TKABR'))
True
print(is_valid_word('HUE','TKABR'))
False
"""
def is_valid_word(word:str, tiles:str)->bool:
    for i in word:
        if i in tiles:
            tiles = tiles.replace(i,"",1)
        else:
            return False
    return True


"""def remove_element(nums:list,val:int)->int:
Given a list nums and a value val, remove all instances of that value in-place and return the new length of nums list.

Do not allocate extra space for another list, you must do this by modifying the input list in-place with O(1) extra memory.

For example:

Test	Result
nums = [3,2,2,3]
print(remove_element(nums,3),nums)
2 [2, 2]
nums = [0,1,2,2,3,0,4,2]
print(remove_element(nums,2),nums)
5 [0, 1, 3, 0, 4]
"""
def remove_element(nums:list, val:int)->int:
    length = len(nums)
    while(True):
        if val in nums:
            nums.remove(val)
        else:
            break
    return len(nums)