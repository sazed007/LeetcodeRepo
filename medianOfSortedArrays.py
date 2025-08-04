class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array for binary search optimization
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2  # Partition point for nums1
            j = (m + n + 1) // 2 - i  # Partition point for nums2

            # Handle edge cases for i and j to prevent index out of bounds
            # left1, left2 are the largest elements in the left partitions
            # right1, right2 are the smallest elements in the right partitions
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Check if the partitions are correct
            if left1 <= right2 and left2 <= right1:
                # We have found the correct partitions
                # Case 1: Total number of elements is odd
                if (m + n) % 2 == 1:
                    return max(left1, left2)
                # Case 2: Total number of elements is even
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                # The partition in nums1 is too far right
                high = i - 1
            else:  # left2 > right1
                # The partition in nums1 is too far left
                low = i + 1
        
        return 0.0 # Should not be reached