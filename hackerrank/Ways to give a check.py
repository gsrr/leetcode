#!/bin/python

import sys

def checkmate(key, cp):
    steps = [(-1, -1), (-1, 1)]
    for x, y in steps:
        nx = key[0] + x
        ny = key[1] + y
        if cp.get((nx, ny), "None") == "k":
            return True
    return False

def bishop(x, y, kx, ky, cp):
    step = (0, 0)
    if ky > y:
        step = (1, 1)
    else:
        step = (1, -1)
    nx = x + step[0]
    ny = y + step[1]
    while nx != kx and ny != ky:
        if cp.has_key((nx, ny)) and cp((nx, ny)) != "None":
            return 0
        nx = nx + step[0]
        ny = ny + step[1]
    return 2
        
def hook(x, y, kx, ky, cp):
    step = (0, 0)
    if x == kx:
        if ky > y:
            step = (0, 1)
        else:
            step = (0, -1)
    else:
        step = (1, 0)
    nx = x + step[0]
    ny = y + step[1]
    while nx != kx or ny != ky:
        if cp.has_key((nx, ny)) and cp[(nx, ny)] != "None":
            return 0
        
        nx = nx + step[0]
        ny = ny + step[1]
    return 2

def knight(x, y, kx, ky, cp):
    for nx, ny in [(x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]:
        if nx == kx and ky == ky:
            return 1
    return 0
    
def check_king(key, king, cp):
    nx = key[0] - 1
    ny = key[1]
    diffx = abs(king[0] - nx)
    diffy = abs(king[1] - ny)
    if diffx == diffy:
        #print "bishop"
        return bishop(nx, ny, king[0], king[1], cp)
    if diffx == 0 or diffy == 0:
        #print "hook", nx, ny
        return hook(nx, ny, king[0], king[1], cp)
    if (diffx == 1 and diffy == 2) or (diffx == 2 and diffy == 1):
        #print "knight"
        return knight(nx, ny, king[0], king[1], cp)
    return 0

def discoverd_check_b(king, cp, enemy):
    cnt = 0
    kx = king[0]
    ky = king[1]
    steps = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for step in steps:
        nx = kx + step[0]
        ny = ky + step[1]
        while nx >= 0 and ny >= 0 and nx < 8 and ny < 8:
            if cp.has_key((nx, ny)):
                if cp[(nx, ny)] in enemy:
                    return 4
                    break
                else:
                    if cp[(nx, ny)] == "None":
                        pass
                    else:
                        break
            nx += step[0]
            ny += step[1]
    return 0

def discoverd_check_r(king, cp, enemy):
    cnt = 0
    kx = king[0]
    ky = king[1]
    steps = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    for step in steps:
        nx = kx + step[0]
        ny = ky + step[1]
        while nx >= 0 and ny >= 0 and ny < 8 and nx < 8:
            if cp.has_key((nx, ny)):
                if cp[(nx, ny)] in enemy:
                    return 4
                    break
                else:
                    if cp[(nx, ny)] == "None":
                        pass
                    else:
                        break
            nx += step[0]
            ny += step[1]
    return 0

def waysToGiveACheck(board):
    # Complete this function
    king = []
    myking = []
    cp = {}
    for i in xrange(len(board)):
        for j in xrange(len(board[i])):
            if board[i][j] != '#':
                cp[(i, j)] = board[i][j]
            if board[i][j] == 'k':
                king = [i, j]
            if board[i][j] == 'K':
                myking = [i, j]
    cnt = 0
    for key in cp.keys():
        if cp[key] != 'P':
            continue
        if key[0] != 1:
            continue
        if cp.has_key((key[0] - 1, key[1])):
            continue
        '''
        if checkmate(key, cp) == True:
            #cnt += 1
            continue
        '''
        cp[key] = "None"
        if discoverd_check_b(myking, cp, ["q", "b"]) != 0 or discoverd_check_r(myking, cp, ["q", "r"]) != 0:
            cp[key] = "P"
            continue
        if discoverd_check_b(king, cp, ["Q", "B"]) != 0 or discoverd_check_r(king, cp, ["Q", "R"]) != 0:
            return 4
        return check_king(key, king, cp)
        #cp[key] = "P"
    return cnt
        
if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        board = []
        for board_i in xrange(8):
            board_temp = raw_input().strip()
            board.append(board_temp)
        result = waysToGiveACheck(board)
        print result


