class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        num_X=0
        num_O=0
        for i in range(3):
            for j in range(3):
                if board[i][j]=="X":
                    num_X+=1
                elif board[i][j]=="O":
                    num_O+=1
        
        if not (num_X==num_O or num_X==num_O+1):
            return False
        
        if self.check(board,"X"):
            if num_X!=num_O+1:
                return False
        if self.check(board,"O"):
            if num_X!=num_O:
                return False
            if self.check(board,"X"):
                return False
        return True
    def check(self,board,char):
        for i in range(3):
            if board[i][0]==char and board[i][1]==char and board[i][2]==char:
                return True
            if board[0][i]==char and board[1][i]==char and board[2][i]==char:
                return True
        if board[1][1]==char and board[1][1]==board[0][0] and board[1][1]==board[2][2]:
            return True
        if board[1][1]==char and board[1][1]==board[0][2] and board[1][1]==board[2][0]:
            return True
        