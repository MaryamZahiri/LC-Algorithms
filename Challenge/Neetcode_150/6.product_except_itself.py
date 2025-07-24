from typing import List 
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        result = [1] * length
        pre_val, post_val = 1, 1
        for i in range(length):
            result[i] *= pre_val
            pre_val *= nums[i]
            result[length - i - 1] *= post_val
            post_val *= nums[length - i - 1]
        return result
    '''
    O(N), O(1)
    '''
        
    def productExceptSelf2N(self, nums: List[int]) -> List[int]:
        length = len(nums) 
        result = [1] * length
        pre_val = 1
        for i in range(length):
            result[i] *= pre_val
            pre_val *= nums[i]
        pre_val = 1
        for i in range(length - 1, -1, -1):
            result[i] *= pre_val
            pre_val *= nums[i]
        return result
    '''
    1,2,3,4
          i
    result
    24,12,8,6
    pre
    24
    
    '''
        
    def productExceptSelf3N(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1] * length
        postfix = [1] * length
        result = [1] * length

        for i in range(1,length):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(length):
            result[i] = prefix[i] * postfix[i]
        
        return result   
    '''
    [1,2,3]
     i 
    pre
    [1,1,2]
    post
    [6,3,1]
    result
    [6,3,2]
    '''
    def productExceptSelfBF(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for i in range(len(nums)):
            # reset the product
            product = 1
            for j in range(len(nums)):
                # pass index itself
                if i == j: continue
                product *= nums[j]
            result[i] = product
        return result
    '''
    [1,2,3,4]
         i
           j
    product
    8
    result
    24,12,8,..
    '''
'''
[1, 2, 3,4]
[24,12,8,6]

[0,-1]
[-1,0]
'''
'''
BF: O(n^2) O(n)
[1,2,3,4]
     i
        j
 j -> continue

 Pre postfix: O(3n->n) O(3n->n)
 [1,2,3,4]
  i
 pre
 [1,1,2,6]
 post
 [24,12,4,1]
 product
 [24,12,8,6]

 Pre Postfix: O(2n -> n) O(2n -> n)
 [1,2,3,4]
  i
  pre
  [1,1,2,6]
  product
  [24,12,8,6]

  Pre Postfix: O(2n -> n) O(n -> 1)
  [1,2,3,4]
   i
   product
   [1,1,2,6]
   product
   [24,12,8,6]
   post: 12
'''