class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        res =[]

        for i in range(len(gas)):
            stock = 0
            flag = 0
            for j in range(i,i + len(gas)):
                curr= j%len(gas)
                # print(i, curr)
                # print('start',i,'curr', curr,'stock',stock, 'gas availbale',gas[curr],'total stock',stock + gas[curr], 'cost',cost[curr])
                stock = stock + gas[curr] - cost[curr]
                
                if stock >= 0:
                    flag = 1
                else:
                    # print('cant be started from here ',i,gas[i])
                    flag = 0
                    break
            if flag ==1:
                res.append(i)
        # print(res)

        if len(res)==0:
            return -1

        return res[0]
            
