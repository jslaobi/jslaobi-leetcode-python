class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        时间复杂度: O(n)。
        空间复杂度: O(1)。
        """
        # 使用双指针: read和write
        read = 0
        write = 0
        n = len(chars)

        while read < n:
            curr_char = chars[read]
            count = 0

            while read < n and chars[read] == curr_char:
                read += 1
                count += 1
            
            chars[write] = curr_char
            write += 1

            # count有可能是两位数, 所以这里要写一个for循环
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
            
        return write