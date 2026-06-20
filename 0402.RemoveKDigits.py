class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        """
        时间复杂度: O(n)，
        空间复杂度: O(1)。
        """
        stack = []
        # 我们要移除前面尽可能大的数, 比如num = "14329", k = 2. 即使9最大,但是129却是最优解. 但是我们也不能仅仅移除最前面的数,比如329并不是最优解
        # 所以我们利用一个stack,一旦发现stack里的数比当前的数大,就移除并且k-1,直到移除k个数. 也就是发现当前数大于右边的数就移除
        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        
        # 如果到了最后k还没有减完, 则从末尾减掉剩余k个数字(因为这时候stack是升序,所以末尾的数大)
        if k > 0:
            stack = stack[:-k]
        
        result = "".join(stack).lstrip("0")

        return result if result else "0"

            