class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1.extend(nums2)
        while True:
            if len(nums1) > (m+n):
                nums1.remove(0)
            if len(nums1) < (m+n):
                nums1.append(0)
            if len(nums1) == (m+n):
                break
        nums1.sort()