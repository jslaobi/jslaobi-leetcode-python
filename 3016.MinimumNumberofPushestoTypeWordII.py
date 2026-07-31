class Solution:
    def minimumPushes(self, word: str) -> int:
        """时间复杂度: O(n + k log k)。
        空间复杂度: O(k)。
        """
        freq = Counter(word)

        sorted_counts = sorted(freq.values(), reverse=True)

        total_pushes = 0

        for i, count in enumerate(sorted_counts):
            # 0-7应该放在第一位, //8后等于0, +1就是需要按键的次数
            pushed_needed = (i // 8) + 1
            total_pushes += count * pushed_needed
        
        return total_pushes