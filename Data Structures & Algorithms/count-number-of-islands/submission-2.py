class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m = len(grid[0])
        n = len(grid)
        v = [[0 for _ in range(m)] for _ in range(n)]

        def cal_dfs(i,j,g):
            cases =[[i-1,j],[i+1,j],[i,j+1],[i,j-1]]
            print(cases)

            for k in cases:
                if (k[0]>=0 and k[0] < n) and (k[1]>=0 and k[1] < m):
                    # print("Cases before visisted are ",k ,"and visted is ", v[k[0]][k[1]], 'and grid is ', g[k[0]][k[1]] )
                    if v[k[0]][k[1]]!=1 and g[k[0]][k[1]]!='0':
                        print("Cases are ",k)
                        v[k[0]][k[1]]=1
                        cal_dfs(k[0],k[1],g)


        output = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!='0' and v[i][j]!=1:
                    print("grid value ",grid[i][j],"i ,j value ", i, j)
                    v[i][j] = 1
                    cal_dfs(i,j,grid)
                    output = output + 1
        
        print(output)
        return output