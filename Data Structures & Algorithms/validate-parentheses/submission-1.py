class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_to_open = {')':'(','}':'{',']':'['}
        for paren in s:
            if paren in close_to_open:
                if stack and stack[-1] == close_to_open[paren]:
                    stack.pop()
                else:
                    return False
            else: 
                stack.append(paren)
            
        return True if not stack else False

        