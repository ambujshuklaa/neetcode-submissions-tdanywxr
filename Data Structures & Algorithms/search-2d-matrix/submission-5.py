class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = 0 
        c= 0

        while (r < len(matrix)):

            if target > matrix[r][-1]:
                r = r + 1
            elif target < matrix[r][-1] and target > matrix[r][0]:
                break
            elif target == matrix[r][0] or target == matrix[r][-1]:
                return True
            else:
                return False
        
        if r >= len(matrix):
            print ( r)
            return False
        else:
            data = matrix[r]

            l = 0
            r = len(data)-1
            print(data)

            while (l<=r):

                mid = int((l + r ) / 2)

                if target > data[mid]:
                    l = mid + 1
                elif target < data[mid]:
                    r = mid - 1
                else:
                    return True
            
        return False





