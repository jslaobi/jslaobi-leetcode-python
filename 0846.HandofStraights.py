from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """时间复杂度: O(n log n)。
        空间复杂度: O(n)。
        """
        # 如果总牌数不能被groupSize整除,则不成立
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)

        sorted_count = sorted(count)

        for card in sorted_count:
            # 有可能card在之前的循环被消耗掉了,所以要检查一下是否大于0
            if count[card] > 0:
                num_sequences = count[card]

                for i in range(card, card + groupSize):
                    # 根据规则, 数字必须要连续. 所以如果以这个数字起始, 接下来必须有足够的groupSize个连续数字.
                    # 如果card在之前的序列被用到, 会在之前的循环中被减去, 不影响此次循环. 
                    if count[i] < num_sequences:
                        return False
                    
                    count[i] -= num_sequences
        
        return True