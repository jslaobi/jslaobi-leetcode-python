class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        result = []

        start = 0
        end = 0

        for i, char in enumerate(s):
            # 一边读取s里的字符, 一边检查是否需要继续向右移动end
            end = max(end, last_occurrence[char])

            if i == end:
                # 如果i跟end相等,就可以截取下来添加到result里了
                result.append(end-start+1)
                # start移动到i+1的位置
                start = i + 1
        
        return result



        
