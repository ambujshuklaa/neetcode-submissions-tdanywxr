class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        m = len(text1)+1
        n = len(text2)+1
        text1="-"+text1
        text2=","+text2

        dist = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(1,m,1):
            for j in range(1,n,1):
                print('i,j', i,j)
                if text1[i]==text2[j]:
                    dist[i][j]=dist[i-1][j-1] + 1
                else:
                    dist[i][j]=max(dist[i-1][j], dist[i][j-1])

        print(dist[m-1][n-1])

        return dist[m-1][n-1]

