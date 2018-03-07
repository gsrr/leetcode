def diag_arr(board):
    ret = []
    tmp = []
    i = 0
    for x in board:
        tmp.append(x[i])
        i += 1
    ret.append("".join(tmp))
    tmp = []
    i = len(board) - 1
    for x in board:
        tmp.append(x[i])
        i -= 1
    ret.append("".join(tmp))
    return ret

def trans_arr(board):
    return [ "".join([ x[i] for x in board]) for i in xrange(len(board))]


def ans1(board):
    for x in board:
        print x
    ret = []
    ret.extend(board)
    ret.extend(trans_arr(board))
    ret.extend(diag_arr(board))
    cntx = 0
    cnto = 0
    print ret
    for s in ret:
        if s == "XXX":
            cntx += 1
        elif s == "OOO":
            cnto += 1
    if cntx > 0 and cnto > 0:
        return False

    dic = collections.defaultdict(int)
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            c = board[i][j]
            dic[c] += 1

    if dic["X"] - dic["O"] != 0 and dic["X"] - dic["O"] != 1:
        return False
    
    if cntx == 1 and dic["X"] - dic["O"] == 0:
        return False
    
    if cnto== 1 and dic["X"] - dic["O"] == 1:
        return False
    return True

class Solution(object):
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        return ans1(board)
