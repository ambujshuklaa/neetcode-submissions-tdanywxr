class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        final= sorted(intervals + [newInterval])

        l=[]
        start = final[0][0]
        end = final[0][1]

        for i in range (1,len(final),1):
            print('starting start', start,'end',end,'next is',final[i][0])
            if final[i][0]<=end:
                end= max(end, final[i][1])
                print('continue end',end)
            else:
                l.append([start,end])
                start=final[i][0]
                end= final[i][1]
        l.append([start,end])
        print(l)
        return l

            


        