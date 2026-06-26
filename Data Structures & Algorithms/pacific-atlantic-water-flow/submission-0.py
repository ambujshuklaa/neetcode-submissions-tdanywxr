class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])

        visited = [[0 for _ in range(n)] for _ in range(m)]
        output=[]

        pacific=0
        atlantic=0

        def cal_dfs(i,j,m,n,heights):
            nonlocal pacific
            nonlocal atlantic
            childs = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            # print('childs are',childs,i,j)
            visited[i][j]=1
            relevant_childs=[]
    
            for c in childs:
                # print('child are',c,c[0],c[1])
                if c[0]<0 or c[1] < 0:
                    pacific=1
                    # print('pacific',pacific)
                    continue
                elif c[0]>=m or c[1]>=n:
                    atlantic =1
                    # print('atlantic',c,i,j)
                    # print('atlantic',atlantic)
                    continue
                elif visited[c[0]][c[1]]!=1:
                    # print('calling is done from', i,j)
                    if heights[i][j]>=heights[c[0]][c[1]]:
                        relevant_childs.append(c)
                        # print('relevant childs',relevant_childs)

            if len(relevant_childs)==0:
                return 
            
            for r in relevant_childs:
                # print('calling for relevant childs',r)
                cal_dfs(r[0],r[1],m,n,heights)

        for i in range(m):
            for j in range(n):
                visited[i][j]=1
                cal_dfs(i,j,m,n,heights)
                print('for i , j',i,j,'pacific and atlantic are',pacific,atlantic)
                if pacific==1 and atlantic==1:
                    output.append([i,j])
                pacific=0
                atlantic=0
                visited = [[0 for _ in range(n)] for _ in range(m)]
        print(output)

        return output
                
        
        


            






        