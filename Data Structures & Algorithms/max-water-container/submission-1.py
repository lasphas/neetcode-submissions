class Solution:
    def maxArea(self, height: List[int]) -> int:

        l = 0 
        r = len(height) - 1

        max_ar = 0
        while l<r :
            area = (r - l)*min(height[l],height[r])
            if area > max_ar :
                max_ar = area
            if height[l] <= height[r] :
                l += 1
            else :
                r -= 1
        return max_ar