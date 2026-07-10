class Solution:
    def depthSum(self, nestedList: list['NestedInteger']) -> int:
        """时间复杂度: O(n)。
        空间复杂度: O(h)。
        """
        def dfs(nested_list, depth):
            total = 0

            for element in nested_list:
                if element.isInteger():
                    total += element.getInteger() * depth
                else:
                    total += dfs(element.getList(), depth + 1)
            
            return total

        # 根节点深度为1
        return dfs(nestedList, 1)