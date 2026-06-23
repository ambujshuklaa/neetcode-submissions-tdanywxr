class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        key_dict={}

        for i in times:
            if i[0] in key_dict.keys():
                l=[]
                l.append(i[1:])
                key_dict[i[0]]=key_dict[i[0]] + l
            else:
                l=[]
                l.append(i[1:])
                key_dict[i[0]]=l
        
        # print(key_dict)

        import heapq
        pq = []

        visited = [0] * (n+1)
        dist = [999] * (n+1)

        heapq.heappush(pq,[0,k])
        dist[k]=0

        while(len(pq)!=0):
            poped=heapq.heappop(pq)
            node=poped[1]
            # print('node is ',node, poped)

            if visited[node]==0:
                parent_dist = dist[node]
                visited[node]=1

                if node in key_dict.keys():
                    for c in key_dict[node]:
                        child_node_dist=c[1]
                        child_node=c[0]
                        cal_dist = min(parent_dist + child_node_dist, dist[child_node])
                        dist[child_node]=cal_dist
                        heapq.heappush(pq,[cal_dist,child_node])
        
        # print(visited[1:])
        # print(dist[1:])

        if min(visited[1:])==0:
            return -1
        else:
            return max(dist[1:])




            






        