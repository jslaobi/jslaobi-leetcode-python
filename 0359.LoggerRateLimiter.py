class Logger:
    def __init__(self):
        """
        时间复杂度: O(n)，
        空间复杂度: O(n)。
        """
        # Dictionary to store {message: next_allowed_timestamp}
        self.message_dict = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        # 如果是旧消息
        if message in self.message_dict:
            # 检查是否已经过去10秒
            if timestamp >= self.message_dict[message]:
                # 允许并更新下一次允许的时间
                self.message_dict[message] = timestamp + 10
                return True
            else:
                # 依然还在冷却时间中
                return False
        else:
            # 新消息, 直接允许并设置下一次允许的时间
            self.message_dict[message] = timestamp + 10
            return True