'''Sliding Window Maximum
nums=[1,3,-1,-3,5,3,6,7]

k=3
Expected
[3,3,5,5,6,7]
Use deque.
'''


from collections import deque

nums = [1,3,-1,-3,5,3,6,7]
k = 3

def sliding_window_max(nums,k):
    result = []
    window = deque()

    for i in range(nums):

        while window and window[0] < i-k:
            

