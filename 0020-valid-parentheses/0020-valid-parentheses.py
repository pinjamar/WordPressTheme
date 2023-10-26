class Solution:
    def isValid(self, recenica: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for c in recenica:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False