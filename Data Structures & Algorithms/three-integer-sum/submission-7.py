class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # i=0
        # j=0

        # key_dict={}
        # key_dict[0]=[]

        # while(i < len(nums)-2):
        #     j=i+1
            
        #     for j in range(j, len(nums)-1,1 ):
        #         for k in range(j+1,len(nums),1):
        #             print(i,j,k)
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 # print([nums[i], nums[j], nums[j+1]], i,j,j+1)
        #                 # key_dict[i,j,j+1] = [nums[i], nums[j], nums[j+1]]
        #                 key_dict[0] = key_dict[0] + [[nums[i], nums[j], nums[k]]]
                    
        #     i=i+1

        # l=[]

        # for i in key_dict[0]:
        #     if sorted(i) not in l:
        #         l.append(sorted(i))
        
        # print(l)

        # return l

        nums= sorted(nums)
        key_dict={}
        key_dict[0]=[]

        for i in range(0, len(nums)-2,1):

            j=i+1
            k=len(nums)-1

            while(j< k):

                if nums[i] + nums [j] + nums[k]==0:
                    key_dict[0] = key_dict[0] + [[nums[i], nums[j], nums[k]]]
                    j=j+1
                    k=k-1
                
                elif nums[i] + nums [j] + nums[k] > 0:
                    k=k-1
                
                else:
                    j=j+1
        
        l=[]

        for i in key_dict[0]:
            if sorted(i) not in l:
                l.append(sorted(i))
        
        print(l)
        return l
            






                    
            
            




