from typing import List
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        key_dict = {}

        for i in range(len(points)):
            key_dict[i] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):

                dist = abs(points[i][0] - points[j][0]) + \
                       abs(points[i][1] - points[j][1])

                key_dict[i].append([j, dist])
                key_dict[j].append([i, dist])

        pq = []

        visited = [0] * len(points)

        heapq.heappush(pq, [0, 0, -1])

        dist = 0

        while pq:

            weight, node, parent = heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = 1
            dist += weight

            for child_node, child_weight in key_dict[node]:

                if visited[child_node] == 0:
                    heapq.heappush(
                        pq,
                        [child_weight, child_node, node]
                    )

        return dist