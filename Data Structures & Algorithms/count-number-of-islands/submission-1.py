class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # v=[[0]*len(grid[0])]*len(grid)

        m = len(grid[0])
        n = len(grid)
        v = [[0 for _ in range(m)] for _ in range(n)]

        def cal_dfs(ii,jj,g):
            cases =[[ii-1,jj],[ii+1,jj],[ii,jj+1],[ii,jj-1]]
            print(cases)

            total_ans = 0

            for k in cases:
                if (k[0]>=0 and k[0] < n) and (k[1]>=0 and k[1] < m):
                    # print("Cases before visisted are ",k ,"and visted is ", v[k[0]][k[1]], 'and grid is ', g[k[0]][k[1]] )
                    if v[k[0]][k[1]]!=1 and g[k[0]][k[1]]!='0':
                        print("Cases are ",k)
                        v[k[0]][k[1]]=1
                        flag = cal_dfs(k[0],k[1],g)
                        total_ans = flag + 1

            return total_ans


        output = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]!='0' and v[i][j]!=1:
                    print("grid value ",grid[i][j],"i ,j value ", i, j)
                    v[i][j] = 1
                    flag = cal_dfs(i,j,grid)
                    output = output + 1
        
        print(output)
        return output