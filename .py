class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        Row=len(img)
        Col=len(img[0])
        matrix=copy.deepcopy(img)
        def isValid(r,c):
            return 0 <= r < Row and 0 <= c < Col
        
        def sum(r,c):
            total=img[r][c]
            count=1
            adi=[(r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),(r+1,c-1),(r+1,c),(r+1,c+1)]
            for row,col in adi:
                if isValid(row,col):
                    total+=img[row][col]
                    count+=1
            return total//count

        for r in range(Row):
            for c in range(Col):
                matrix[r][c]=sum(r,c)
        return matrix
        
