class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        key_dict={}
        
        for i in range(len(points)):
            key_dict[i] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                dist = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])

                key_dict[i].append([j, dist])
                key_dict[j].append([i, dist])
        
        # print(key_dict)

        import heapq
        pq = []

        visited = [0] * (len(key_dict) +1)
        # mst = [] * (len(key_dict) +1)

        heapq.heappush(pq,[0,0,-1])

        dist=0

        while(len(pq)!=0):
            poped=heapq.heappop(pq)
            node=poped[1]
            parent=poped[2]
            weight = poped[0]
            if visited[node]==1: continue
            visited[node]=1
            dist = dist + weight
            # if poped[2]!=-1:
            #     comb=[]
            #     comb.append([parent,node])
            #     mst.append(comb)

            if node in key_dict.keys():
                for c in key_dict[node]:
                    parent_node =node
                    child_node=c[0]
                    if visited[child_node]==0:
                        child_weight=c[1]
                        heapq.heappush(pq,[child_weight,child_node, parent_node])

        # print(dist)
        # print(mst)

        return dist



        