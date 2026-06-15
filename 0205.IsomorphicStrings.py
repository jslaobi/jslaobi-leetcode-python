class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # # 题目最下面保证了两个字符串长度相等,所以不需要
        # if len(s) != len(t):
        #     return False
        # 这里需要双向查找, 比如"ab"和"xx", 单向a->x, b->x,但是反向查找时就会发现多对一的问题
        map_s_to_t = {}
        map_t_to_s = {}

        for i in range(len(s)):
            if s[i] in map_s_to_t and map_s_to_t.get(s[i]) != t[i]:
                return False
            if t[i] in map_t_to_s and map_t_to_s.get(t[i]) != s[i]:
                return False           
            
            map_s_to_t[s[i]] = t[i]
            map_t_to_s[t[i]] = s[i]
        
        return True

