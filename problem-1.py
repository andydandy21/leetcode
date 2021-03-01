#Two Sum
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = 0      
        y = 1
        while nums[x] + nums[y] != target:
          if y == len(nums)-1:
            x += 1
            y = x+1
          else: 
            y += 1
        return [x,y]