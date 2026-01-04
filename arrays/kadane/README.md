# Kadane’s Algorithm
  Kadane's algorithm is an efficient dynamic programming algorithm used to find the maximum sum of a contiguous subarray within a given one-dimensional array of numbers. It operates in linear time, O(n), and uses constant space, O(1), making it much faster than brute-force or divide-and-conquer methods for the same problem. How it Works : 
   The algorithm works by iterating through the array once, keeping track of two main variables: 
   max_current: The maximum sum of a subarray ending at the current position.
   max_so_far: The overall maximum sum encountered anywhere in the array so far. 
   At each element, the algorithm decides whether it is better to start a new subarray (with the current element alone) or to extend the current one. If the current sum becomes negative, it resets, as a negative sum will not contribute positively to a future maximum sum. 
   Algorithm Steps Initialize max_so_far and max_current to the first element of the array(ex:nums[0]). (Some variations initialize to 0 or negative infinity depending on whether empty subarrays are allowed).Iterate through the array starting from the second element.
   For each current_element, update max_current to the maximum of:The current_element itself.max_current + current_element.
   Update max_so_far to be the maximum of max_so_far and max_current.Return max_so_far after the loop finishes. 
   
   Example : Consider the array [-2, 1, -3, 4, -1, 2, 1, -5, 4].
   i      x     cur_sum(cur_sum = max(x,cur_sum+x))      max_sum      
   0      -2    -2                                        -2             Intialize
   1       1     max(1,-2+1) = 1                         max(-2,1)=1     start new sub array
   2      -3     max(-3,-3+1) = -2                       max(1,-2)=1     cur_max is negative
   3       4     max(4,-2+4) = 4                         max(1,4)=4      start new sub array
   4      -1     max(-1,-1+4)=3                          max(4,3)=4      extend sub array
   5       2     max(2,2+3) = 5                          max(4,5)=5      extend sub array
   6       1     max(1,1+5)=6                            max(6,5)=6      extend sub array
   7      -5     max(-5,-5+6)=1                          max(6,1)=6      extend sub array
   8       4     max(4,4+1)=5                            max(6,5)=6      extend sub array
The final answer is 6, which corresponds to the subarray [4, -1, 2, 1]. 
## When to use
- Maximum / minimum subarray problems
- Continuous subarrays
- Optimization over linear scan

## Core Idea
At each index, decide:
- Extend the previous subarray
- Or start a new subarray

## Template
curr = nums[0]
best = nums[0]

         range(1,len(nums))
for x in nums[1:]:
    curr = max(x, curr + x)
    best = max(best, curr)

## Variations
- Maximum product subarray
- Minimum subarray
- Circular subarray

## Common mistakes
- Initializing with 0 instead of nums[0]
- Forgetting all-negative arrays

## Edge cases 
- A. negative numbers [-3,-2,-5 ] answer = -2 #we intialize nums[0] not 0
- B. zeros included nums [0,-1,0 ] answer = 0