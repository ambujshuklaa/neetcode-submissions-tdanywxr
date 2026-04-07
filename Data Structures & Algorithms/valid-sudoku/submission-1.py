class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkDuplicate(l) -> bool:
            key_dict={}
            for i in l:
                if (i in key_dict.keys()) and i !=".":
                    return False
                elif i !=".":
                    key_dict[i]=1
            
            return True


        for i in range (0, len(board),1):
            flag = checkDuplicate(board[i])
            if flag == False:
                return False

        for i in range (0, len(board),1):
            data = []
            for j in range (0, len(board),1):
                data.append(board[j][i])

            flag = checkDuplicate(data)
            if flag == False:
                return False

        key_dict_output={}        

        for i in range (0, len(board),1):
            for j in range (0, len(board),1):
                # print(i,j,int(i/3),int(j/3))
                if (int(i/3),int(j/3)) in key_dict_output.keys() and board[i][j]!=".":
                    l= []
                    l.append(board[i][j])
                    key_dict_output[int(i/3),int(j/3)]= key_dict_output[int(i/3),int(j/3)] + l
                elif board[i][j]!=".":
                    l= []
                    l.append(board[i][j])
                    key_dict_output[int(i/3),int(j/3)]= l


        # print(key_dict_output.keys())
        
        for i in key_dict_output.keys():
            print(key_dict_output[i])
            flag = checkDuplicate(key_dict_output[i])
            print(flag)
            if flag == False:
                return False
        
        return True


                
        
        

                               
        
        

        

