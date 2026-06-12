class Solution:
    def isValid(self, s: str) -> bool:
        paren = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        stack = []

        for p in s:
            if p in paren:
                stack.append(p)
            else:
                if not stack:
                    return False
                left = stack.pop()
                if p != paren[left]:
                    return False

        return len(stack) == 0