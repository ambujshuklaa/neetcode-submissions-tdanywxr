class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m = len(grid[0])
        n = len(grid)
        v = [[0 for _ in range(m)] for _ in range(n)]

        ans = 0
        # ct = 0


        def cal_dfs(i,j,g):
            nonlocal ct
            cases =[[i-1,j],[i,j+1],[i+1,j],[i,j-1]]
            print(cases)

            for k in cases:
                if (k[0]>=0 and k[0] < n) and (k[1]>=0 and k[1] < m):
                    if v[k[0]][k[1]]!=1 and g[k[0]][k[1]]!=0:
                        v[k[0]][k[1]]=1
                        ct = ct + 1
                        cal_dfs(k[0],k[1],g)

        output = []
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and v[i][j]!=1:
                    v[i][j] = 1
                    ct = 1
                    cal_dfs(i,j,grid)
                    output.append(ct)
                    
                    
        if len(output)==0:
            return 0
        return max(output)