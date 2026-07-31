class Codec:
    def encode(self, strs: List[str]) -> str:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        encoded_strings = []
        for s in strs:
            # 示例: "hello" 变成 "5#hello"
            encoded_strings.append(f"{len(s)}#{s}")

        return "".join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        """时间复杂度: O(n)。
        空间复杂度: O(n)。
        """
        decoded_strings = []
        i = 0

        while i < len(s):
            # 寻找下一个#的位置
            j = s.find('#', i)
            # 读取长度
            length = int(s[i:j])

            string_start = j + 1
            string_end = string_start + length
            decoded_strings.append(s[string_start:string_end])

            i = string_end

        return decoded_strings
