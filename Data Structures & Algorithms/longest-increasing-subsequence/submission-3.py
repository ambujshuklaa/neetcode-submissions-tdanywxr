class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # sorted_array = sorted([(p,s) for p,s in zip(nums, range(len(nums)))])

        # print(sorted_array)

        # key_dict={}

        # for i in sorted_array:
        #     key_dict[i[0]]=i[1]

        # print(key_dict)

        # prev=-1
        # cnt = 0
        # l=[]

        # for i in key_dict.keys():
        #     if key_dict[i] > prev:
        #         cnt= cnt + 1
        #     # else:
        #     #     l.append(cnt)
        #     #     cnt= 0
        #     prev=max(key_dict[i],prev)
        
        # print(cnt)
        # return cnt

        # cnt = 0
        # for i in range(len(nums)-1,-1,-1):
        #     print(i)
        #     if nums[i-1] < nums[i]:
        #         cnt= cnt + 1
        
        # print(cnt)
        # return cnt


        # arr = [0]*len(nums)

        # for i in range(len(nums)-1, -1,-1):
        #     if i==len(nums)-1:
        #         arr[i]=1
        #     else:
        #         j =i + 1
        #         l=[1]
        #         while(j<len(nums)):
        #             if nums[i]< nums[j]:
        #                 l.append(arr[j]+1)
        #             # print(l)
        #             arr[i]=max(l)
        #             j= j+ 1
                    
        
        # print(arr)

        # return max(arr)

        arr = [0]*len(nums)

        for i in range(len(nums)-1, -1,-1):
            if i==len(nums)-1:
                arr[i]=1
            else:
                j = i + 1
                max_val = 1
                while(j< len(nums)):
                    if nums[i]<nums[j]:
                        max_val= max(max_val, 1,1+arr[j])
                    j= j+1
                arr[i]=max_val
        
        print(arr)

        return max(arr)






            



        