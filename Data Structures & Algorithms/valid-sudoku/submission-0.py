class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = defaultdict(set)
        row = defaultdict(set)
        sq = defaultdict(set)
        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == '.':
                    continue
                if cur in row[i] or cur in col[j] or cur in sq[(i // 3, j // 3)]:
                    return False
                row[i].add(cur)
                col[j].add(cur)
                sq[(i // 3, j // 3)].add(cur)
        return True