class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for op in operations:
            if '+' in op:
                x += 1
            else:
                x -= 1
        return x             
       #  return sum(1 if op[1] == "+" else -1 for op in operations)