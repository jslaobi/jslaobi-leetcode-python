from collections import defaultdict

class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        substring_counts = defaultdict(int)
        result = []

        for s in arr:
            # substring可能有重复, 使用set去重
            # 去重的原因是,我们不希望将同一个string中的substring统计多次,比如aba,我们应该只记录一次a而不是两次
            unique_substrings = set()

            # 区间的右边是开区间,所以for j in range(i+1, len(s) + 1)不包括len(s) + 1, s[i:j]不包括len(s)
            for i in range(len(s)):
                for j in range(i+1, len(s) + 1):
                    unique_substrings.add(s[i:j])
            
            # 统计substring出现次数
            for substring in unique_substrings:
                substring_counts[substring] += 1
        
        
        # 找到数组里每个单词的最短子字符串,添加到结果
        for s in arr:
            shortest = ""
            for i in range(len(s)):
                for j in range(i+1, len(s) + 1):
                    substring = s[i:j]

                    if substring_counts[substring] == 1:
                        # 更新shortest的三种情况: shortest为空, 新的substring长度更小, 长度相等但是substring字符更靠前
                        if not shortest or len(substring) < len(shortest) or (len(substring) == len(shortest) and substring < shortest):
                            shortest = substring
            result.append(shortest)
        
        return result

