class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[]
        postfix = [0 for _ in range(len(nums))]

        for i in nums:
            if len(prefix)==0:
                prefix.append(i)
            else:
                prefix.append(i*prefix[len(prefix)-1])
                
        print(prefix)

        for i in range(len(nums)-1,-1,-1):
            if i ==len(nums)-1:
                # print(len(nums)-1,nums[i])
                postfix[len(nums)-1]=nums[i]
            else:
                # print(postfix, i , nums[i])
                postfix[i]=nums[i] * postfix[i+1]

        print(postfix)
        output=[]
        for i in range(0,len(nums),1):
            if i ==0:
                output.append(1*postfix[i+1])
            elif i == len(nums)-1:
                output.append(1*prefix[i-1])
            else:
                output.append(prefix[i-1] * postfix[i+1])
        print(output)
        return output
