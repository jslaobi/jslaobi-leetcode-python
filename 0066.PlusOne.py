class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1

        for i in range(length, -1, -1):
            # 检查最后一位是否为9,如果不是9则加1并终止循环立刻返回结果
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # 否则就将9变为0,然后继续循环,检查前一位
            digits[i] = 0
        # 如果循环结束还没返回,说明是99999这种情况,需要加一位    
        return [1] + digits