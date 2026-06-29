from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        counts = Counter(nums)
        max_length = 1

        # 处理1这个特殊情况, 因为1的多少次方都是1, 所以我们数有多少个1
        # 因为成立的答案的元素个数一定是奇数个,所以如果1的数量是偶数,count-1
        if 1 in counts:
            if counts[1] % 2 == 0:
                max_length = max(max_length, counts[1] - 1)
            else:
                max_length = max(max_length, counts[1])
        
        for num in counts:
            if num == 1:
                continue
            
            curr_len = 0
            curr_num = num

            # 我们需要一头一尾两个相同的数
            while counts[curr_num] >= 2:
                curr_len += 2
                curr_num = curr_num * curr_num
            
            # 最后我们检查不满足条件的第一个数是否至少有一个用来作为峰值
            # 如果满足条件,比如2,2,4, 4不满足counts[curr_num] >= 2, 但是可以用来作为2,4,2的峰值,所以curr_len += 1
            if counts[curr_num] >= 1:
                curr_len += 1
            # 反之, 比如2,2,4,4, 第一个不满足的数是16,我们没有16所以要用4作为峰值
            # 之前一步我们执行了curr_len += 2, 但是实际上我们只能用1个4. 所以这里curr_len -= 1
            else:
                curr_len -= 1

            max_length = max(max_length, curr_len)
        
        return max_length