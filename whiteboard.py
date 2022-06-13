# In this little assignment you are given a list of numbers, and have to return the highest and lowest number in a string separated by a single space.

# Example:
# high_and_low([1, 2, 3, 4, 5])  # return "5 1"
# high_and_low([1, 2, -3, 4, 5]) # return "5 -3"
# high_and_low([1, 9, 3, 4, -5) # return "9 -5"

# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.

def maxmin(array):
    return f"{max(array)} {min(array)}"

print(maxmin([1, 9, 3, 4, -5]))

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1

# ex.1
# Input: s = "leetcode"
# Output: 0

# ex.2
# Input: s = "loveleetcode"
# Output: 2

# ex.3
# Input: s = "aabb"
# Output: -1

def indexer(st):
    dict = {}
    a = -1
    for x in st:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    for i in range(len(st)):
        if dict[st[i]] == 1:
            a = i
            return a  
    return a