class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        print(paths)
        for cur in paths:
            if stack and cur == "..":
                stack.pop()
                continue
            if cur == '.':
                continue
            if cur != "" and cur != "..":
                stack.append(cur)
        print(stack)
        return '/' + "/".join(stack)