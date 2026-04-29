class Solution:
    def isValid(self, s: str) -> bool:
        bracket_dict = {"(": ")", "{": "}", "[": "]"}

        str_stack = []
        for i in range(len(s)):
            if s[i] in ("}", ")", "]"):
                if len(str_stack) == 0:
                    return False
                if s[i] == bracket_dict[str_stack[-1]]:
                    str_stack.pop()
                else:
                    return False
            if s[i] in ("{", "(", "["):
                str_stack.append(s[i])

        return False if len(str_stack) > 0 else True
        
        