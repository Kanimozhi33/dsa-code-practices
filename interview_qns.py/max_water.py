class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) -1
        max_water = 0
        while left<right:
            width = right-left
            curr_ht = min( height[right],height[left])
            area = width * curr_ht
            max_water = max(area, max_water)
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return max_water
            
# js
# /**
#  * @param {number[]} height
#  * @return {number}
#  */
# var maxArea = function(height) {
#     let left = 0;
#     let right = height.length-1;
#     let maxWater = 0;
#     while (left <right){
#         let width = (right-left);
#         let currHt = Math.min(height[left], height[right]);
#         let area = width*currHt;
#         maxWater = Math.max(area,maxWater);
#         if (height[left] < height[right]){
#             left ++;
#         }
#         else{
#             right--;
#         }
#     }
#     return maxWater;
# };