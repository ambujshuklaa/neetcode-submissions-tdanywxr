class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        dist = [[999 for _ in range(n)] for _ in range(m)]


        def cal_bfs(i,j):

            queue.append([i,j])
            # print("2 wala element in queue is",queue )

            while (len(queue) > 0):
                e = queue.popleft()
                visited[e[0]][e[1]]=1

                cases = [[e[0]-1, e[1]],[e[0]+1,e[1]],[e[0],e[1]-1],[e[0],e[1]+1]]
                child = []

                for c in cases:
                    # print("child are", c)
                    if (c[0]>=0 and c[0]<m) and (c[1]>=0 and c[1]<n):
                        if visited[c[0]][c[1]]!=1 and grid[c[0]][c[1]]!=2 and grid[c[0]][c[1]]!=0 :
                            child.append(c)
                # print("Child are ",child)
                
                for kids in child:
                    distance = max(abs(e[0]-kids[0]), abs(e[1]-kids[1])) + dist[e[0]][e[1]]
                    dist[kids[0]][kids[1]]=min(dist[kids[0]][kids[1]], distance)
                    # print("Distance is ",distance)
                    queue.append([kids[0],kids[1]])
                
                

        for i in range(m):
            for j in range(n):
                print(i,j)
                if grid[i][j]==2 and visited[i][j]!=1:
                    # print("start dfs algo at index", i,j ,"and value is",grid[i][j] )
                    dist[i][j]=0
                    cal_bfs(i,j)
                    visited = [[0 for _ in range(n)] for _ in range(m)]

        ans=0

        for i in range(m):
            for j in range(n):
                if dist[i][j]==999 and grid[i][j]==1:
                    return -1
                if dist[i][j]!=999 and dist[i][j]!=0 :
                    ans=max(ans,dist[i][j])
            

        return ans

        


        
        
       

