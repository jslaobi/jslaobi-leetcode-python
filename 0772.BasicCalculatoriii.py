import collections

class Solution:
    def calculate(self, s: str) -> int:
        # Step 1: Remove all spaces and convert the string into a Queue
        # deque (Double Ended Queue) allows O(1) pops from the left side
        s = s.replace(" ", "")
        q = collections.deque(s)
        
        # Step 2: Create our recursive helper function
        def helper(q):
            stack = []
            current_num = 0
            last_sign = '+'
            
            while len(q) > 0:
                char = q.popleft()
                
                # Build the number just like LC 227
                if char.isdigit():
                    current_num = current_num * 10 + int(char)
                    
                # RECURSION: If we hit '(', solve the sub-problem!
                if char == '(':
                    current_num = helper(q)
                    
                # If we hit an operator, a closing ')', or the queue is finally empty
                # Notice this is a separate 'if', avoiding your previous 'elif' bug!
                if char in "+-*/)" or len(q) == 0:
                    if last_sign == '+':
                        stack.append(current_num)
                    elif last_sign == '-':
                        stack.append(-current_num)
                    elif last_sign == '*':
                        stack.append(stack.pop() * current_num)
                    elif last_sign == '/':
                        # Safely handle Python's negative division
                        stack.append(int(stack.pop() / current_num))
                        
                    # Update the sign and reset the number
                    last_sign = char
                    current_num = 0
                    
                    # If we hit a closing parenthesis, this sub-problem is done. Break the loop!
                    if char == ')':
                        break
                        
            # Sum up everything left in the stack for this scope
            return sum(stack)
            
        return helper(q)