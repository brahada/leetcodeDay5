class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums: List[int]) -> float:
        nums2=nums+nums1
        nums2=sorted(nums2)
        n=len(nums2)
        if len(nums2)%2==0:
            med=(nums2[n//2]+nums2[(n//2)-1])/2
        else:
            med=nums2[n//2]
        return med
