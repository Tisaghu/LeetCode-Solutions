class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rowHash = {i:[] for i in range(0,9)}
        colHash = {i:[] for i in range(0,9)}

        #divide into 9 boxes
        boxHash = {i:[] for i in range(1,10)}


        for row in range(0,9):
            for col in range(0,9):
                val = board[row][col]
                #check for number
                if val != ".":
                    #check if number already in row or col hash
                    if val in rowHash[row] or val in colHash[col]:
                        return False
                    #check if number already in 3x3 box
                    boxRow = (row // 3) + 1
                    boxCol = (col // 3) + 1
                    boxNum = (boxRow - 1) * 3 + boxCol
                    if val in boxHash[boxNum]:
                        return False
                    boxHash[boxNum].append(val)
                    #add to both hashmaps
                    rowHash[row].append(val)
                    colHash[col].append(val)
        
        return True




test = Solution()

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(test.isValidSudoku(board)) #true

board2 = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(test.isValidSudoku(board2)) #false

board3 =[[".",".","4",".",".",".","6","3","."],
         [".",".",".",".",".",".",".",".","."],
         ["5",".",".",".",".",".",".","9","."],
         [".",".",".","5","6",".",".",".","."],
         ["4",".","3",".",".",".",".",".","1"],
         [".",".",".","7",".",".",".",".","."],
         [".",".",".","5",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

print(test.isValidSudoku(board3)) #should be false, got true