class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        n = len(nums)
        # 用来存储是否与target数字相同的次数
        freq = defaultdict(int)

        # 当前有多少个多出的与target数字相等的
        curr = 0
        freq[0] = 1

        smaller_count = 0
        total_subarrays = 0

        for num in nums:
            if num == target:
                # 如果找到了一个跟target数字相等的, 加到smaller_count里,并且curr加1
                smaller_count += freq[curr]
                curr += 1
            else:
                smaller_count -= freq[curr - 1]
                curr -= 1
        
            total_subarrays += smaller_count

            freq[curr] += 1
        
        return total_subarrays