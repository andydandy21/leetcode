#4. Median of Two Sorted Arrays   


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        mylist = nums1 + nums2
        mylist.sort()
        r = m+n+1
        p = r//2
        if r%2 != 0:
            median = (mylist[p-1]+mylist[p]) / 2
        else:
            median = mylist[p-1]
        return median