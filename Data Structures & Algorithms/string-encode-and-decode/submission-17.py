class Solution:

    def encode(self, strs: List[str]) -> str:
        # output=""
        # if strs!=[]:
        #     for i in strs:
        #         for j in i:
        #             output= output + "," + str(ord(j))
        #         output=output + "/"
        #     print(output,output[:-1]) 
        #     return output[:-1] 
        # else:
        #     return ""

        output = ""
        for i in strs:
            output = output + str(len(i)) + "#" + i 
        
        # print(output)
        return output




    def decode(self, s: str) -> List[str]:
        # l=[]
        # print(s)
        # if s!="":
        #     for i in s.split("/"):
        #         output=""
        #         for j in i.split(","):
        #             if j !="":
        #                 output=output + chr(int(j))
        #         l.append(output)
        # return l

        l= []

        i = 0

        while (i<len(s)):
            j = i
            while(s[j]!='#'):
                j = j + 1
            length = int(s[i:j])
            l.append(s[j+1: j+1 + length])
            print(length, i ,j)
            i = j + 1 + length

        return l

