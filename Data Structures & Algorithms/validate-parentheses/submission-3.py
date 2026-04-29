class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"{": "}", "(": ")", "[": "]"}
        str_stack = []

        for char in s:
            if char in bracket_dict:
                str_stack.append(char)
            elif char in ("}", ")", "]"):
                if not str_stack or bracket_dict[str_stack.pop()] != char:
                    return False
        
        return not str_stack