class Solution(object):
    def isValidSudoku(self, board):
        
        
        #check each row
        for eachRow in board:
            test = [0] * 9
            for item in eachRow:
                if item != '.':
                    num = int(item) - 1
                    count = test[num] + 1
                    if count > 1:
                        return False
                    else:
                        test[num] = count
        
        #check each column
        for j in range(9):
            test = [0] * 9
            for i in range(9):
                item = board[i][j]
                if item != '.':
                    num = int(item) - 1
                    count = test[num] + 1
                    if count > 1:
                        return False
                    else:
                        test[num] = count
                        
        
        #check each block
        for i in range(0,9,3):
            for j in range(0,9,3):
                test = [0] * 9
                for m in range(3):
                    for n in range(3):
                        item = board[i+m][j+n]
                        if item != '.':
                            num = int(item) - 1
                            count = test[num] +1
                            if count > 1:
                                return False
                            else:
                                test[num] = count
        
        return True