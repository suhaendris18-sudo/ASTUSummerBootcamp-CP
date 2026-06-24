class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        s=len(score)
        for r in range(s):
            for c in range(r+1,s):
                if score[r][k]< score[c][k]:
                    score[r],score[c] = score[c], score[r]
        return score             
        