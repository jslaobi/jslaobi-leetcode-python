class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        arr.sort()

        # 第一个元素一定是1
        curr = 1

        # 虽然看上去条件很复杂,但其实就是如果当前的数arr[i]等于curr就用arr[i](因为是排序的,所以不会更小), 如果更大就用curr+1(如例子2, 100->2, 1000->3)
        for i in range(1, len(arr)):
            curr = min(curr+1, arr[i])
        
        return curr